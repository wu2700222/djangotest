# -*- coding: utf-8 -*-
 
from django.shortcuts import render
# from django.views.decorators import csrf
from django.http import HttpResponse
# @csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置django.middleware.csrf.CsrfViewMiddleware全局中间件。
# @csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了django.middleware.csrf.CsrfViewMiddleware全局中间件。
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# 接收POST请求数据
def post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)

@csrf_exempt
def hello(request):
    if request.POST:
        aa = request.POST['q']
        return HttpResponse(aa)
    else:
        return HttpResponse('非法请求,请加入参数q')