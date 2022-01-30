from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mp_id>[0-9]+)/mp/$', views.mp, name='mp'),
    url(r'^(?P<constituency_id>[0-9]+)/constituency/$', views.constituency, name='constituency'),
    url(r'^(?P<work_id>[0-9]+)/work/$', views.work, name='work'),
    url(r'^(?P<item_id>[0-9]+)/feedback/$', views.feedback, name='feedback'),
    url(r'^(?P<item_id>[0-9]+)/(CONSTITUENCY)/feedback/$', views.feedback, {'item': 'CONSTITUENCY'}, name='feedback'),
    url(r'^(?P<item_id>[0-9]+)/(WORK)/feedback/$', views.feedback, {'item': 'WORK'}, name='feedback'),
]