#正常操实体机器操作

#安装类django
pip3 install django==2.0.7
#进入项目目录，再使用启动命令
nohup python3 manage.py runserver 0.0.0.0:8080 &

nohup python3 manage.py runserver 0.0.0.0:8081 &
nohup python3 manage.py runserver 0.0.0.0:8082 &
nohup python3 manage.py runserver 0.0.0.0:8083 &
#测试
https://dev-qll.otosaas.com/search-post

#打包成镜像步骤
#1.进入项目根目录(和dockerfile同一个目录)
#2.生成配置，pip3 freeze > requirements.txt，删除不必要的外包，编写dockerfile文件
#3.执行命令打包docker build -t dockertest:0.1 .
#4.启动镜像docker run -p 8080:8080 -d --name test dockertest:0.1