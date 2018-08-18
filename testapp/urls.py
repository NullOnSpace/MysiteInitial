from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^base/$', views.base, name='base'),
    url(r'^login/$', views.login_v1, name='login'),
    url(r'^logout/$', views.logout_v1, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^main/$', views.main, name='main'),
    url(r'^management/$', views.management, name='mana'),
    url(r'^community/$', views.community, name='com'),
    url(r'^dm-get/$', views.dm_get, ),
    url(r'^living-get/$', views.living_get, ),
    url(r'^nickname-get/$', views.nickname_get, ),
    url(r'^spe-follow-get/$', views.spe_follow_get, ),
    url(r'^room-json-get/$', views.room_json_get, ),
    url(r'^comment-get/$', views.comment_get, ),
    url(r'^grant/$', views.grant, ),
]
