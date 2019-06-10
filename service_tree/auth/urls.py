# coding=utf-8

from django.urls import path
from . import views

urlpatterns = [
    path('status', views.Status.as_view(), name='status'),

    path('token/<str:token_id>', views.SSO.as_view(), name='tree_auth'),
]
