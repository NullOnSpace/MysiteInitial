from django.contrib import admin
from .models import Main, Historyname, Icon, Noblelist, Event, Band, \
        Bandname, Club, Clubmember, Giftrecord, Gift, Liveroom
import datetime
from django.utils.translation import ugettext_lazy as ul
from django.db.models import Count

# Register your models here.


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    def noblelevel(self, obj):
        qs = Noblelist.objects.filter(uid=obj.uid)
        if qs:
            nl = qs.order_by('-accesstime').first().nl
            r = Noblelist.NOBLENAME[
                    list(zip(*Noblelist.NOBLENAME))[0].index(nl)][1]
        else:
            r = 'unknown'
        return r

    def dttime(self, obj):
        return datetime.datetime.fromtimestamp(int(obj.lastaccess))

    list_display = ('uid', 'nickname', 'level',
                    'isgirl', 'noblelevel', 'dttime', )
    search_fields = ('nickname', )
    list_per_page = 20

"""
@admin.register(Noblelist)
class NobleAdmin(admin.ModelAdmin):
    def nickname(self, obj):
        return Main.objects.get(uid=obj.uid).nickname

    def dttime(self, obj):
        return datetime.datetime.fromtimestamp(int(obj.accesstime))

    list_display = ('uid', 'nickname', 'nl', 'dttime')
    search_fields = ('uid',)
    list_filter = ('nl',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def operator(self, obj):
        return Main.objects.get(uid=obj.sid).nickname

    def accepter(self, obj):
        if obj.oid:
            return Main.objects.get(uid=obj.oid).nickname
        else:
            return '-'

    def dttime(self, obj):
        return datetime.datetime.fromtimestamp(int(obj.optime))

    list_display = ['operator', 'accepter', 'msgtype', 'roomid', 'dttime']
    list_filter = ('msgtype', 'roomid')


class BandBidFilter(admin.SimpleListFilter):
    title = ul('bandname')
    parameter_name = 'bid'

    def lookups(self, request, model_admin):
        bids = tuple(str(x['bid']) for x in
                     Band.objects.values('bid').annotate(
                         num_bids=Count('bid')).filter(num_bids__gt=1000))
        bcounts = tuple(Band.objects.filter(bid=z).count() for z in bids)
        bnames = tuple(
            Bandname.objects.get(id=y).bandname
            if Bandname.objects.filter(id=y).count() else 'unknown'+y
            for y in bids)
        retList = list(zip(bids, map(ul, bnames), bcounts))
        retList.sort(key=lambda ele: ele[2], reverse=True)
        retTP = tuple(map(lambda x: (x[0], x[1]), retList[:30]))
        return retTP

    def queryset(self, request, queryset):
        return queryset.filter(bid=self.value())


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    def nickname(self, obj):
        return Main.objects.get(uid=obj.uid).nickname

    def bandnn(self, obj):
        return Bandname.objects.get(id=obj.bid).bandname

    list_display = ['nickname', 'bandnn', 'bdlv']
    list_filter = [BandBidFilter, ]


@admin.register(Bandname)
class BandnameAdmin(admin.ModelAdmin):
    def get_bcount(self, obj):
        return Band.objects.filter(bid=obj.id).count()
    get_bcount.short_description = 'FANNUMBER'

    list_display = ['roomid', 'bandname', 'get_bcount', 'regtime']
    search_fields = ['bandname', ]


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    def nickname(self, obj):
        return Main.objects.get(uid=obj.ownerid).nickname
    list_display = ['cid', 'logo', 'nickname', 'cname']
    readonly_fields = ['cid', 'ownerid']
    ordering = ['cid']


@admin.register(Clubmember)
class ClubmemberAdmin(admin.ModelAdmin):
    def nickname(self, obj):
        return Main.objects.get(uid=obj.uid).nickname
    list_display = ['nickname', 'cid']
    list_filter = ['cid']


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ['gid', 'giftname', 'gifttype', 'contrib', 'desc', 'intro',
                    'hititv']


@admin.register(Giftrecord)
class GiftrecordAdmin(admin.ModelAdmin):
    def nickname(self, obj):
        return Main.objects.get(uid=obj.uid).nickname

    def giftname(self, obj):
        return Gift.objects.get(gid=obj.gid).giftname

    def dttime(self, obj):
        return datetime.datetime.fromtimestamp(int(obj.sendtime))

    list_display = ['nickname', 'giftname', 'dttime', 'roomid', 'maxhits']
    list_filter = ['gid']
"""

admin.site.register((Historyname, Icon, Liveroom))
