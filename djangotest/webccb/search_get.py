# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
#参考资料http://www.runoob.com/django/django-form.html
#表单
def search_form(request):
    return render_to_response('get.html')

#接受请求数据
def get(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message='参数g的内容为：'+request.GET['q']
    else:
        message='没有获取到g参数'
    return HttpResponse(message)