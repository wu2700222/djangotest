# -*- coding: utf-8 -*-
 
from django.shortcuts import render
# from django.views.decorators import csrf
from django.http import HttpResponse
# @csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置django.middleware.csrf.CsrfViewMiddleware全局中间件。
# @csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了django.middleware.csrf.CsrfViewMiddleware全局中间件。
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
import http.client
#参考资料http://www.runoob.com/django/django-form.html
# 接收POST请求数据
def post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['bodys']
    return render(request, "post.html", ctx)

@csrf_exempt
def hello(request):
    if request.method == "POST" :
        #获取body中的数据
        body = request.POST['bodys']
        #获取head中的数据
        HTTP_RID=request.META.get("HTTP_RID")
        return HttpResponse("获取body中的数据q:"+body+"\n获取head中的数据HTTP_RID:"+HTTP_RID)
    else:
        return HttpResponse('非法请求,请加入参数q')

@csrf_exempt
def getrid(request):
    if request.method == "POST" :
        #获取body中的数据
        body = request.POST['bodys']
        #获取head中的数据
        HTTP_RID=request.META.get("HTTP_RID")

        headers = {'Content-type': 'application/json','RID':HTTP_RID} 
        bodyvalues = {
        'token':'123456',
        'phone_num':'13817552207'
        }

        response=post_api(request,'/qlltest1',headers,bodyvalues)
        return HttpResponse("接口返回值:"+response.read().decode())
    else:
        return HttpResponse('非法请求,请加入参数bodys')

def post_api(request,apipath,headers,bodyvalues):
    
    # connection = http.client.HTTPSConnection('127.0.0.1:8080')
    connection = http.client.HTTPConnection('127.0.0.1:8080')
    headers = headers
    json_foo = json.dumps(bodyvalues)
    connection.request('POST', apipath, json_foo, headers)
    return connection.getresponse()
