# coding=utf-8

import json
from django.views import View
from utils.response import MyResponse
from .models import UserModel, PermissionModel, RoleModel, RolePermissionModel, UserRoleModel

class Status(View):

    def get(self, request):
        data = {}
        # 拼接返回值
        response = MyResponse().succeed(data)
        return response

class User(View):

    user_name = ''

    def dispatch(self, request, *args, **kwargs):
        self.user_name = self.kwargs['user_name']
        obj = super(User,self).dispatch(request, *args, **kwargs)
        return obj

    # 查看
    # GET /auth/user/user_name 基于user_name查看用户信息
    def get(self, request, *args, **kwargs):
        # 处理数据
        data = UserModel().get(self.user_name)
        # 拼接返回值
        response = MyResponse().succeed(data)
        return response

    # 增加
    # POST /auth/user/user_name 增加用户信息
    def post(self, request, *args, **kwargs):
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = UserModel().add(self.user_name, requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

    # 修改
    # PUT /auth/user/user_name 修改用户信息
    def put(self, request, *args, **kwargs):
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = UserModel().update(self.user_name, requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

    # 删除
    # DELETE /tree/node/node_name 删除用户
    def delete(self, request, *args, **kwargs):
        # 处理数据
        dbStatus = UserModel().delete(self.user_name)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

class Permission(View):

    permission_id = 0

    def dispatch(self, request, *args, **kwargs):
        if request.method != 'POST':
            self.permission_id = self.kwargs['permission_id']
        obj = super(Permission,self).dispatch(request, *args, **kwargs)
        return obj

    # 查看
    # GET /auth/permission/permission_id 基于permission_id查看权限信息
    def get(self, request, *args, **kwargs):
        # 处理数据
        data = PermissionModel().get(self.permission_id)
        # 拼接返回值
        response = MyResponse().succeed(data)
        return response

    # 增加
    # POST /auth/permission/ 增加权限信息
    def post(self, request, *args, **kwargs):
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = PermissionModel().add(requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

    # 删除
    # DELETE /auth/permission/permission_id 删除权限信息
    def delete(self, request, *args, **kwargs):
        # 处理数据
        dbStatus = PermissionModel().delete(self.permission_id)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

class Role(View):

    role_id = 0

    def dispatch(self, request, *args, **kwargs):
        if request.method != 'POST':
            self.role_id = self.kwargs['role_id']
        obj = super(Role,self).dispatch(request, *args, **kwargs)
        return obj

    # 查看
    # GET /auth/role/role_id 基于role_id查看角色信息
    def get(self, request, *args, **kwargs):
        # 处理数据
        data = RoleModel().get(self.role_id)
        # 拼接返回值
        response = MyResponse().succeed(data)
        return response

    # 增加
    # POST /auth/role/ 增加角色信息
    def post(self, request, *args, **kwargs):
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = RoleModel().add(requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

    # 修改
    # PUT /auth/role/role_id 修改角色信息
    def put(self, request, *args, **kwargs):
        # 解析body数据
        requestData = json.loads(request.body)
        # 处理数据
        dbStatus = RoleModel().update(self.role_id, requestData)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

    # 删除
    # DELETE /auth/role/role_id 删除角色信息
    def delete(self, request, *args, **kwargs):
        # 处理数据
        dbStatus = RoleModel().delete(self.role_id)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

class RolePermission(View):

    role_id = 0
    permission_id = 0

    def dispatch(self, request, *args, **kwargs):
        self.role_id = self.kwargs['role_id']
        if request.method == 'POST' or request.method == 'DELETE':
            self.permission_id = self.kwargs['permission_id']
        obj = super(RolePermission,self).dispatch(request, *args, **kwargs)
        return obj

    # 查看
    # GET /auth/role/role_id/permission/ 基于role_id查看权限信息
    def get(self, request, *args, **kwargs):
        # 处理数据
        data = RolePermissionModel().get(self.role_id)
        # 拼接返回值
        response = MyResponse().succeed(data)
        return response

    # 增加
    # POST /auth/role/role_id/permission/permission_id 增加权限信息
    def post(self, request, *args, **kwargs):
        # 处理数据
        dbStatus = RolePermissionModel().add(self.role_id, self.permission_id)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

    # 删除
    # DELETE /auth/role/role_id/permission/permission_id 删除权限信息
    def delete(self, request, *args, **kwargs):
        # 处理数据
        dbStatus = RolePermissionModel().delete(self.role_id, self.permission_id)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

class UserRole(View):

    user_name = ''
    server_name = ''
    role_id = 0

    def dispatch(self, request, *args, **kwargs):
        self.user_name = self.kwargs['user_name']
        self.server_name = self.kwargs['server_name']
        if request.method == 'POST' or request.method == 'DELETE':
            self.role_id = self.kwargs['role_id']
        obj = super(UserRole,self).dispatch(request, *args, **kwargs)
        return obj

    # 查看
    # GET /auth/user/user_name/server/server_name/role/ 基于user_name查看角色信息
    def get(self, request, *args, **kwargs):
        # 处理数据
        data = UserRoleModel().get(self.user_name, self.server_name)
        # 拼接返回值
        response = MyResponse().succeed(data)
        return response

    # 增加
    # POST /auth/user/user_name/server/server_name/role/role_id 增加角色信息
    def post(self, request, *args, **kwargs):
        # 处理数据
        dbStatus = UserRoleModel().add(self.user_name, self.server_name, self.role_id)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response

    # 删除
    # DELETE /auth/user/user_name/server/server_name/role/role_id 删除角色信息
    def delete(self, request, *args, **kwargs):
        # 处理数据
        dbStatus = UserRoleModel().delete(self.user_name, self.server_name, self.role_id)
        # 拼接返回值
        if dbStatus == 'succeed':
            response = MyResponse().succeed({})
        else:
            response = MyResponse().failed('process failed')
        return response
