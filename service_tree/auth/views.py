# coding=utf-8

from utils.response import MyResponse
from django.views import View
from .models import Token

class Status(View):

    def get(self, request):
        data = {}
        # 拼接返回值
        response = MyResponse().succeed(data)
        return response

class SSO(View):

    token_id = ''

    def dispatch(self, request, *args, **kwargs):
        self.token_id = self.kwargs['token_id']
        obj = super(SSO,self).dispatch(request, *args, **kwargs)
        return obj

    # 查看
    # GET /auth/token/token_id 基于token_id查看是否登陆 如果登陆则返回用户信息
    def get(self, request, *args, **kwargs):
        userInfo, dbStatus = Token().getInfoByTokenid(self.token_id)
        # 拼接返回值
        if dbStatus == 'succeed':
            # userInfo 为空 未登陆
            if userInfo == {}:
                response = MyResponse().succeed(userInfo)
            # userInfo 不为空 登陆
            else:
                response = MyResponse().succeed(userInfo)
        else:
            response = MyResponse().failed('process failed')
        return response




