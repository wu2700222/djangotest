# -*- coding: utf-8 -*-
 
from django.shortcuts import render
# from django.views.decorators import csrf
from django.http import HttpResponse
# @csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置django.middleware.csrf.CsrfViewMiddleware全局中间件。
# @csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了django.middleware.csrf.CsrfViewMiddleware全局中间件。
from django.views.decorators.csrf import csrf_exempt,csrf_protect
#参考资料http://www.runoob.com/django/django-form.html
import json
import http.client
# 接收POST请求数据

def post_api(request,apipath,headers,bodyvalues):
    
    #外网域名通讯
    #connection = http.client.HTTPSConnection('dev-api.otosaas.com')
    #内网域名通讯
    connection = http.client.HTTPConnection('dev-kong-qllapi.localdomain:8000')
    #内网端口通讯
    # connection = http.client.HTTPConnection('127.0.0.1:8080')
    headers = headers
    json_foo = json.dumps(bodyvalues)
    connection.request('POST', apipath, json_foo, headers)
    return connection.getresponse()

@csrf_exempt
def qlltest1(request):
    if request.method == "POST" :
        #获取body中的数据
        #body = request.POST['bodys']
        #获取head中的数据
        HTTP_RID=request.META.get("HTTP_RID")
        headers = {'Content-type': 'application/json','RID':HTTP_RID}
        
        bodyvalues = {
        'token':'123456',
        'phone_num':'13817552207'
        }

        response=post_api(request,'/qlltest2',headers,bodyvalues)
        # print(HTTP_RID)
        # return HttpResponse('HTTP_RID:'+str(HTTP_RID))
        #post请求下个接口
                # return HttpResponse(response.read().decode())
        #这里得调用qlltest2的api获取数据
        return HttpResponse("\n"+response.read().decode()+"\n qlltest1接口获取head中的数据HTTP_RID:"+HTTP_RID)
    else:
        return HttpResponse('请进行post请求')

@csrf_exempt
def qlltest2(request):
    if request.method == "POST" :
        #获取body中的数据
        #body = request.POST['bodys']
        #获取head中的数据
        HTTP_RID=request.META.get("HTTP_RID")

        headers = {'Content-type': 'application/json','RID':HTTP_RID}
        
        bodyvalues = {
        'token':'123',
        'phone_num':'1234'
        }
        response=post_api(request,'/qlltest3',headers,bodyvalues)

        #这里得调用qlltest3的api获取数据
        return HttpResponse("\n"+response.read().decode()+"\n qlltest2接口获取head中的数据HTTP_RID:"+HTTP_RID)
    else:
        return HttpResponse('请进行post请求')

        
@csrf_exempt
def qlltest3(request):
    if request.method == "POST" :
        #获取body中的数据
        #body = request.POST['bodys']
        #获取head中的数据
        HTTP_RID=request.META.get("HTTP_RID")

        #这里得调用qlltest2的api获取数据
  
        return HttpResponse("qlltest3接口获取head中的数据HTTP_RID:"+HTTP_RID)
    else:
        return HttpResponse('请进行post请求')