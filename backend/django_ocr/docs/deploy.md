### 急速部署
通过 docker 直接启动已经推送到 dockerhub 的镜像：
```
docker run --name django-ocr-server -p 8000:8000 -d choubaodxs/django-ocr:v1.0
```
启动成功后访问 http://127.0.0.1:8000/swagger/ 查看 swagger 文档以及直接测试接口

### 使用 mysql 数据库
默认情况下数据库使用容器内的 sqlite，可以通过配置环境变量使用自己的 mysql 数据库：
```
DB_USE_MYSQL=True # 设置为 True 表示使用 mysql 数据库
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
```
### 其他环境变量
```
DEBUG=False # django 的 DEBUG 设置，默认为 False
OPEN_SWAGGER=True # 是否开放 swagger 接口文档地址，默认为 True
```