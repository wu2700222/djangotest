# 基于的基础镜像
FROM python:3.6.6
# 维护者信息
# MAINTAINER wuwei  wuwei@boluome.com
# 代码添加到code文件夹
COPY . /code
# 设置code文件夹是工作目录
WORKDIR /code
# 安装支持
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
#CMD ["ls", ""]