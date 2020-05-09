# coding=utf-8

import json
from django.utils.deprecation import MiddlewareMixin


class Debug(MiddlewareMixin):

    server_name = 'ncov-api'

    def process_request(self, request):
        request_data = json.loads(request.body)
        print("request_data:", request_data)
