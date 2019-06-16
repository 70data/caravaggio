# coding=utf-8

from django.urls import path
from . import views

urlpatterns = [
    path('status', views.Status.as_view(), name='status'),

    path('user/<str:user_name>', views.User.as_view(), name='auth_user'),

    path('user/<str:user_name>/server/<str:server_name>/role/', views.UserRole.as_view(), name='auth_user'),
    path('user/<str:user_name>/server/<str:server_name>/role/<int:role_id>', views.UserRole.as_view(), name='auth_user'),

    path('permission/', views.Permission.as_view(), name='auth_permission'),
    path('permission/<int:permission_id>', views.Permission.as_view(), name='auth_permission'),

    path('role/', views.Role.as_view(), name='auth_role'),
    path('role/<int:role_id>', views.Role.as_view(), name='auth_role'),

    path('role/<int:role_id>/permission/', views.RolePermission.as_view(), name='auth_role'),
    path('role/<int:role_id>/permission/<int:permission_id>', views.RolePermission.as_view(), name='auth_role'),
]
