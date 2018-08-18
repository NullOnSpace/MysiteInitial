import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.models import User, Group
from .models import Liveroom, Roomfollow, Userfollow, Main, Post
import time
import datetime
import requests
import redis


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('gotta')
    form = forms.ContactForm()
    return render(request, 'index.html', {'form': form})


def logout_v1(request):
    request.COOKIES.clear()
    logout(request)
    return render(request, 'logout.html')


def base(request):
    return render(request, 'base.html')


def register(request):
    if request.method == "GET":
        form = forms.UserFormStrict()
        return render(request, 'uregister.html', {'form': form})
    elif request.method == "POST":
        if request.POST.get('check'):
            form = forms.UserFormStrict()
            field_name = request.POST.get('field')
            field = form.fields.get(field_name)
            value = request.POST.get(field_name)
            data = dict()
            try:
                field.clean(value)
            except ValidationError as e:
                data['fieldError'] = str(e).replace("'", '"')
                data['check'] = 'fail'
            else:
                data['check'] = 'success'
            return HttpResponse(json.dumps(data),
                                content_type="application/json")
        else:
            form = forms.UserFormStrict(request.POST)
            if form.is_valid():
                user = User.objects.create_user(**form.cleaned_data)
                user.groups.add(Group.objects.get(name='Common'))
                return redirect('/testapp/login/')


def login_v1(request):
    form = forms.UserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/testapp/main')
        else:
            return render(request, 'login.html',
                          {'form': form, 'error': 'not match'})
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/testapp/login/')
def main(request):
    user = request.user
    if request.method == "GET":
        rooms_followed = Roomfollow.objects.filter(userid=user.id)
        frm_ids = [room.roomid for room in rooms_followed]
        rooms_followed = Liveroom.objects.filter(roomid__in=frm_ids)
        return render(request, 'umain.html', {'user': user,
                                              'f_rooms': rooms_followed, })


@login_required(login_url='/testapp/login/')
def community(request):
    if request.method == "GET":
        posts_all = Post.objects.filter(refid=-1,
                                        isdeleted=0).order_by('-pubtime')
        p = Paginator(posts_all, 10)
        num = request.GET.get('page', 1)
        page_n = p.page(num)
        posts = page_n.object_list
        for post in posts:
            post.username = User.objects.get(id=post.userid).username
            post.can_delete = True if (
                request.user.has_perm('can_del_all_post') or
                (request.user.has_perm('can_del_ipost') and
                 request.user.id == post.userid)) else False
        return render(request, 'ucommunity.html', {'posts': posts,
                                                   'page': page_n,
                                                   })
    elif request.method == "POST":
        user = request.user
        post_dict = {'userid': user.id,
                     'pubtime': datetime.datetime.today()}
        if request.POST.get('action') == 'post':
            post_dict['refid'] = -1
            post_dict['text'] = request.POST.get('content')
            Post.objects.create(**post_dict)
        elif request.POST.get('action') == 'comment':
            post_dict['refid'] = request.POST.get('refid')
            post_dict['text'] = request.POST.get('content')
            Post.objects.create(**post_dict)
        elif request.POST.get('action') == 'delete':
            post_id = request.POST.get('pid')
            post = Post.objects.get(pk=post_id)
            if user.has_perm('can_del_all_post') or (
                    post.userid == user.id and
                    user.has_perm('can_del_ipost')):
                if not post.isdeleted:
                    post.isdeleted = 1
                    post.delid = user.id
                    post.deltime = datetime.datetime.today()
                    post.save()
                else:
                    return HttpResponse('Error: delete void!')
            else:
                return HttpResponse('Error: no privilege to delete')
        return redirect('/testapp/community/')


@login_required(login_url='/testapp/login/')
def management(request):
    if request.method == "GET":
        user = request.user
        rooms_followed = Roomfollow.objects.filter(userid=user.id)
        users_followed = Userfollow.objects.filter(userid=user.id)
        frm_ids = [room.roomid for room in rooms_followed]
        rooms_followed = Liveroom.objects.filter(roomid__in=frm_ids)
        rooms_rest = Liveroom.objects.exclude(roomid__in=frm_ids)
        fusr_ids = [user.followusr for user in users_followed]
        users_followed = Main.objects.filter(uid__in=fusr_ids)
        return render(request, 'umanage.html', {'user': user,
                                                'f_rooms': rooms_followed,
                                                'uf_rooms': rooms_rest,
                                                'f_users': users_followed,
                                                })
    elif request.method == "POST":
        http_res = user_mana_post(request)
        return http_res


@login_required(login_url='/testapp/login/')
def dm_get(request):
    if request.method == "GET":
        rds = redis.Redis(host='127.0.0.1', port=6379)
        rid = request.GET.get('rid', 0)
        ts = int(request.GET.get('ts', 0))
        msg_no = int(request.GET.get('msgno', 0))
        if rid:
            namepre = 'room'+rid
            if ts:
                tsa = ts
            else:
                tsa = (int(time.time())-2)//100
            msg_pipe = []
            ts_new = ts
            for i in range(tsa, int(time.time())//100+1):
                name = namepre+str(i)
                if rds.exists(name):
                    ts_new = i
                    if i == tsa:
                        res = rds.lrange(name, msg_no, -1)
                        msg_no += len(res)
                    else:
                        res = rds.lrange(name, 0, -1)
                        msg_no = len(res)
                    res_strs = [res_bin.replace(b'\xef\xbc\x9f', b'?').decode()
                                for res_bin in res]
                    res_dicts = [eval(res_str) for res_str in res_strs]
                    msg_pipe.extend(res_dicts)
            data = {'msgpipe': msg_pipe, 'ts': ts_new, 'msgno': msg_no}
            return HttpResponse(json.dumps(data),
                                content_type="application/json")


@login_required(login_url='/testapp/login/')
def living_get(request):
    if request.method == "GET":
        rds = redis.Redis(host='127.0.0.1', port=6379)
        lv_set_bin = rds.smembers('living')
        lv_list = [lv.decode() for lv in lv_set_bin]
        return HttpResponse(json.dumps(lv_list),
                            content_type="application/json")


@login_required(login_url='/testapp/login/')
def comment_get(request):
    if request.method == "GET":
        refid = request.GET.get('refid', 0)
        if refid:
            comments = Post.objects.filter(refid=refid)
            check_list = [comment.id for comment in comments]
            outer_list = check_list.copy()
            data_dict = {cmt.id: {'username':
                                  User.objects.get(pk=cmt.userid).username,
                                  'pubtime': cmt.pubtime, 'thumb': cmt.thumb,
                                  'text': cmt.text,
                                  }
                         for cmt in comments}
            rel_dict = dict()
            while True:
                try:
                    pid = check_list.pop(0)
                except IndexError:
                    break
                else:
                    sub_comments = Post.objects.filter(refid=pid)
                    data_dict.update({
                        cmt.id: {
                            'username':
                            User.objects.get(pk=cmt.userid).username,
                            'pubtime': cmt.pubtime, 'thumb': cmt.thumb,
                            'text': cmt.text,
                            }
                        for cmt in sub_comments})
                    rel_dict[pid] = sub_list = [comment.id
                                                for comment in sub_comments]
                    check_list.extend(sub_list)
        data = {'outer': outer_list, 'cmts': data_dict, 'rel': rel_dict}
        return HttpResponse(json.dumps(data, default=__default),
                            content_type="application/json")


@login_required(login_url='/testapp/login/')
def nickname_get(request):
    if request.method == "GET":
        nn_seg = request.GET.get('nickname', None)
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
        if nn_seg:
            qs = Main.objects.filter(
                nickname__icontains=nn_seg).order_by('-level')
            p = Paginator(qs, 10)
            page_n = p.page(page)
            new_qs = page_n.object_list
            nn_list = [{'uid': obj.uid, 'nn': obj.nickname, 'lv': obj.level}
                       for obj in new_qs]
            data = {'ptotal': p.num_pages, 'pcurrent': page, 'nnlist': nn_list}
        else:
            data = dict()
        return HttpResponse(json.dumps(data),
                            content_type="application/json")


@login_required(login_url='/testapp/login/')
def spe_follow_get(request):
    if request.method == "GET":
        user_id = request.user.id
        if user_id:
            qs = Userfollow.objects.filter(userid=user_id)
            data = [{'uid': obj.followusr}
                    for obj in qs]
        else:
            data = []
        return HttpResponse(json.dumps(data),
                            content_type="application/json")


@login_required(login_url='/testapp/login/')
def room_json_get(request):
    if request.method == "GET":
        rid = request.GET.get('rid')
        url = 'http://open.douyucdn.cn/api/RoomApi/room/' + rid
        res = requests.get(url)
        return HttpResponse(json.dumps(json.loads(res.text)),
                            content_type="application/json")


@login_required(login_url='/testapp/login/')
def grant(request):
    if request.user.has_perm('grant'):
        if request.method == "POST":
            form = forms.PermissionGroupForm(request.POST)
            if form.is_valid():
                group_id = form.cleaned_data['group']
                group = Group.objects.get(pk=group_id)
                try:
                    user = User.objects.get(
                        pk=request.POST.get('user-id', 0))
                except User.DoesNotExist:
                    return HttpResponse("Error in User Not Exists")
                user.groups.set([group])
        objects = User.objects.all().order_by('id')
        p = Paginator(objects, 10)
        num = request.GET.get('page', 1)
        try:
            page_n = p.page(int(num))
        except (EmptyPage, ValueError):
            page_n = p.page(1)
        groups = {v: k for k, v in forms.PermissionGroupForm.Groups}
        default_group = Group.objects.get(name="Common")
        for obj in page_n.object_list:
            if len(obj.groups.all()) != 1:
                obj.groups.set([default_group])
            group = obj.groups.all()[0]
            if group.name in groups:
                obj.group = forms.PermissionGroupForm(
                    initial={'group': groups[group.name]})
            else:
                print('group name out of range',
                      group.name, 'not in', list(groups.iterkeys()))
        return render(request, 'grant.html', {'objs': page_n})
    else:
        return HttpResponse('Havn\'t been granted for grant!')


# Not View Function
def get_recipe(food: str, tms: str):
    tms_dec = int(tms)
    food_hex = int(food, base=16)
    ingre = str(hex(food_hex-tms_dec))[2:]
    return ingre


def user_mana_post(request):
    if request.method != 'POST':
        return HttpResponse(json.dumps({'res': 'fail',
                                        'error': 'method not right'}))
    else:
        user = request.user
        chart = request.POST.get('chart')
        action = request.POST.get('action')
        food = request.POST.get('food')
        tms = request.POST.get('tms')
        info = get_recipe(food, tms)
        CHARTDICT = {
            'Roomfollow': 'roomid',
            'Userfollow': 'followusr',
        }
        extra_info = CHARTDICT.get(chart)
        if not (extra_info and action in ['add', 'del']):
            return HttpResponse(json.dumps({'res': 'fail',
                                            'error': 'para invalid'}))
        else:
            model = eval(chart)
            row_dict = {'userid': user.id, extra_info: info}
            print(info)
            if action == 'add':
                if model.objects.filter(**row_dict).exists():
                    return HttpResponse(json.dumps({'res': 'fail',
                                                    'error': 'item exists'}))
                else:
                    new_line = model(**row_dict)
                    new_line.save()
                    newid = model.objects.get(**row_dict).id
                    return HttpResponse(json.dumps({'res': 'ss',
                                                    'info': str(newid)}))
            elif action == 'del':
                obj = model.objects.filter(**row_dict)
                if obj.exists():
                    obj.delete()
                    return HttpResponse(json.dumps({'res': 'ss',
                                                    'info': 'delete'}))
                else:
                    return HttpResponse(json.dumps({'res': 'fail',
                                                    'info': 'delete empty'}))
            else:
                return HttpResponse(json.dumps({'res': 'fail',
                                                'error': 'just fuck'}))


def __default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
#    elif isinstance(obj, date):
#        return obj.strftime('%Y-%m-%d')
    else:
        raise TypeError('%r is not JSON serializable' % obj)


# Signals
@receiver(pre_save, sender=Userfollow)
def completion(sender, **kwargs):
    pass
