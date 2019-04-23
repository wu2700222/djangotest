# -*- coding: utf-8 -*-
 
from django.shortcuts import render
# from django.views.decorators import csrf
from django.http import HttpResponse
# @csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置django.middleware.csrf.CsrfViewMiddleware全局中间件。
# @csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了django.middleware.csrf.CsrfViewMiddleware全局中间件。
from django.views.decorators.csrf import csrf_exempt,csrf_protect
#参考资料http://www.runoob.com/django/django-form.html
# 接收POST请求数据
@csrf_exempt
def qlltest1(request):
    if request.method == "POST" :
        #获取body中的数据
        body = request.POST['bodys']
        #获取head中的数据
        HTTP_RID=request.META.get("HTTP_RID")

        #这里得调用qlltest2的api获取数据
        return HttpResponse("获取body中的数据bodys:"+body+"\n获取head中的数据HTTP_RID:"+HTTP_RID)
    else:
        return HttpResponse('非法请求,请加入参数bodys')

