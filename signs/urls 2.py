from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^monday/$', views.showMondayTable(), name='showMonday'),
    url(r'^monday/(?:/(?P<subject_id>[0-9]+))/$', views.showMondayTable, name='showMonday'),
    url(r'^tuesday/$', views.showTuesdayTable, name='showTuesday'),
    url(r'^wednesday/$', views.showWednesdayTable, name='showWednesday'),
    url(r'^thursday/$', views.showThursdayTable, name='showThursday'),
    url(r'^friday/$', views.showFridayTable, name='showFriday'),
    url(r'^mysigns/$', views.mySigns, name='mysigns'),
    url(r'^monday/signme/(?P<subject_id>[0-9]+)/$', views.signMe, name='signMe'),
    url(r'^tuesday/signme/(?P<subject_id>[0-9]+)/$', views.signMe, name='signMe'),
    url(r'^wednesday/signme/(?P<subject_id>[0-9]+)/$', views.signMe, name='signMe'),
    url(r'^thursday/signme/(?P<subject_id>[0-9]+/)$', views.signMe, name='signMe'),
    url(r'^friday/signme/(?P<subject_id>[0-9]+/)$', views.signMe, name='signMe'),
    url(r'signmeout/(?P<sign_id>[0-9]+)/' , views.singMeOut, name='singmeout'),
]
