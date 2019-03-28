from django.conf.urls import url
from . import view,search_get,search_post

urlpatterns=[
    #http://127.0.0.1:8080/hello
    url('hello', view.hello),
    #http://127.0.0.1:8080/get
    #模拟get参数
    url('get', search_get.search_form),
    #http://127.0.0.1:8080/search_get/?q=wuwei   
    #get请求
    url('^search$', search_get.get),
    #post请求 ^ 与 $分别为匹配开始与结束符,精确匹配
    url(r'^search-post$', search_post.post),

    url(r'^posttest$', search_post.hello)
]