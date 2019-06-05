# coding=utf-8

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        next_path = request.path
        upstream_path = '/'.join(next_path.split('/')[:-1])
