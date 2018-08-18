# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines
#       if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models,
#     but don't rename db_table values or field names.
from django.db import models


class Historyname(models.Model):
    uid = models.CharField(max_length=12, blank=True, null=True)
    usedname = models.CharField(max_length=60, blank=True, null=True)
    lastaccess = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'historyname'

    def __str__(self):
        return '{} {} {}'.format(self.uid, self.usedname, self.lastaccess)


class Icon(models.Model):
    uid = models.CharField(max_length=12, blank=True, null=True)
    iconaddr = models.CharField(max_length=70, blank=True, null=True)
    lastaccess = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'icon'

    def __str__(self):
        return self.iconaddr


class Main(models.Model):
    GENDER = (
        (0, 'Male'),
        (1, 'Female'),
    )

    uid = models.CharField(primary_key=True, max_length=12)
    nickname = models.CharField(max_length=40, blank=True, null=True)
    lastaccess = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    isgirl = models.IntegerField(choices=GENDER, blank=True, null=True,
                                 verbose_name='gender')

    class Meta:
        db_table = 'main'

    def __str__(self):
        return self.nickname


class Noblelist(models.Model):
    NOBLENAME = (
        ('0', '未知'),
        ('1', '骑士'),
        ('2', '子爵'),
        ('3', '伯爵'),
        ('4', '公爵'),
        ('5', '国王'),
        ('6', '皇帝'),
        ('7', '游侠'),
        ('-', '普通'),
    )
    uid = models.CharField(max_length=12, blank=True, null=True)
    nl = models.CharField(max_length=1,
                          choices=NOBLENAME, blank=True, null=True)
    accesstime = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'noblelist'

    def __str__(self):
        return '{} {} {}'.format(self.uid, self.nl, self.accesstime)


class Bandname(models.Model):
    roomid = models.IntegerField(blank=True, null=True)
    bandname = models.CharField(max_length=10, blank=True, null=True)
    regtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'bandname'

    def __str__(self):
        return '{:8} {}'.format(self.roomid, self.bandname)


def getbnn():
    bandname = tuple(
        (a, Bandname.objects.get(id=a).bandname)
        for a in map(
            lambda x: x['id'],
            Bandname.objects.values('id')))
    return bandname


class Band(models.Model):
    BANDNAME = getbnn()
    uid = models.CharField(max_length=12)
    bid = models.IntegerField(choices=BANDNAME)
    bdlv = models.IntegerField()
    lastaccess = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'band'

    def __str__(self):
        return '{:12} {:3} {} {}'.format(
            Main.objects.all().get(uid=self.uid).nickname,
            Bandname.objects.all().get(pk=self.bid).bandname,
            self.bdlv,
            self.lastaccess)


class Event(models.Model):
    sid = models.CharField(max_length=12)
    oid = models.CharField(max_length=12, blank=True, null=True)
    msgtype = models.CharField(max_length=20, db_column='type')
    roomid = models.IntegerField(blank=True, null=True)
    optime = models.IntegerField()
    rint = models.IntegerField(blank=True, null=True)
    rstr = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'event'

    def __str__(self):
        return '{} {}'.format(self.id, self.msgtype)


class Club(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=30, blank=True, null=True)
    cicon = models.CharField(max_length=100, blank=True, null=True)
    logo = models.CharField(max_length=4, blank=True, null=True)
    ownerid = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        db_table = 'club'

    def __str__(self):
        return '{} {} {}'.format(self.cid, self.logo, self.ownerid)


def getcnn():
    clubname = tuple((a, Club.objects.get(cid=a).cname)
                     for a in map(lambda x: x['cid'],
                                  Club.objects.values('cid')))
    return clubname


class Clubmember(models.Model):
    CLUBNAME = getcnn()
    uid = models.CharField(max_length=12)
    cid = models.IntegerField(choices=CLUBNAME)

    class Meta:
        db_table = 'clubmember'

    def __str__(self):
        return '{} {}'.format(self.uid, self.cid)


class Giftrecord(models.Model):
    uid = models.CharField(max_length=12)
    gid = models.IntegerField()
    sendtime = models.IntegerField()
    roomid = models.IntegerField()
    maxhits = models.IntegerField()

    class Meta:
        db_table = 'giftrecord'

    def __str__(self):
        return '{} sent {} at {} in {} by {}'.format(
            self.uid, self.gid, self.sendtime, self.roomid, self.maxhits)


class Gift(models.Model):
    GIFTTYPE = (
        (1, 'fishball'),
        (2, 'sharkfin'),
    )
    gid = models.IntegerField(unique=True)
    giftname = models.CharField(max_length=30, blank=True, null=True)
    gifttype = models.SmallIntegerField(choices=GIFTTYPE,
                                        blank=True, null=True)
    contrib = models.IntegerField(blank=True, null=True)
    mimg = models.CharField(max_length=150, blank=True, null=True)
    himg = models.CharField(max_length=150, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)
    intro = models.CharField(max_length=60, blank=True, null=True)
    hititv = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'gift'


class Danmu(models.Model):
    uid = models.CharField(max_length=12)
    dmid = models.IntegerField()
    chattime = models.IntegerField()
    roomid = models.IntegerField()

    class Meta:
        db_table = 'danmu'


class Danmuid(models.Model):
    chatmsg = models.CharField(max_length=600)

    class Meta:
        db_table = 'danmuid'


class Liveroom(models.Model):
    roomid = models.IntegerField()
    ownernn = models.CharField(max_length=40)

    class Meta:
        db_table = 'liveroom'


class Roomfollow(models.Model):
    userid = models.IntegerField()
    roomid = models.IntegerField()

    class Meta:
        db_table = 'roomfollow'


class Userfollow(models.Model):
    userid = models.IntegerField()
    followusr = models.CharField(max_length=12)

    class Meta:
        db_table = 'userfollow'


class Post(models.Model):
    userid = models.IntegerField()
    refid = models.IntegerField()
    pubtime = models.DateTimeField()
    thumb = models.IntegerField(default=0)
    text = models.TextField(max_length=140, blank=True)
    btext = models.BinaryField(max_length=560, blank=True)
    istext = models.BooleanField(default=True)
    isdeleted = models.BooleanField(default=False)
    delid = models.IntegerField(blank=True, null=True)
    deltime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'post'
