# coding=utf-8

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect
from auth.models import PermissionModel, UserRoleModel, RolePermissionModel

class AuthMiddleware(MiddlewareMixin):

    server_name = 'tree'

    def process_request(self, request):
        requestPath = request.path
        # 取最后一个字符
        last = requestPath[-1]
        # 如果是 / 则认为是资源
        if last == '/':
            server_uri = last
        # 如果不是 / 则删除最后一个分割段落
        else:
            server_uri = '/'.join(requestPath.split('/')[:-1]) + '/'
        # 获取数据
        user_name = 'yuchang'
        # 校验
        # `user_id` `server_name` 取得 `role_id`列表-A
        roleList = UserRoleModel().get(user_name, self.server_name)
        # `server_name` `method` `url` 取得 `permission_id`
        permissionID = PermissionModel().getPermissionid(self.server_name, request.method, server_uri)
        # `permission_id` 取得 `role_id`列表-B
        roleListFull = RolePermissionModel().getRoleids(permissionID)
        # `role_id`列表-A 是否在 `role_id`列表-B中
        for one_role in roleList:
            roleID = one_role['role_id']
            for i in roleListFull:
                if roleID == i:
                    print('token succeed')
                    break
        print('token faild')
