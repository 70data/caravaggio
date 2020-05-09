# coding=utf-8

from django.urls import path

from .views import status, user, count, sample, region

urlpatterns = [
    path('status', status.status, name='status'),

    path('user/register', user.user_register, name='user'),
    path('user/update', user.user_update, name='user'),
    path('user/info', user.user_info, name='user'),
    path('user/login', user.user_login, name='user'),

    path('count/insert', count.count_insert, name='count'),
    path('count/update', count.count_update, name='count'),
    path('count/delete', count.count_delete, name='count'),
    path('info/getCount', count.count_info, name='count'),

    path('sample/insert', sample.sample_insert, name='count'),
    path('sample/update', sample.sample_update, name='count'),
    path('sample/delete', sample.sample_delete, name='count'),
    path('info/getPat', sample.sample_info, name='count'),

    path('region/insert', region.region_insert, name='count'),
    path('info/getNextLoc', region.region_next, name='count'),
]
