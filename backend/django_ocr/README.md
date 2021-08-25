### 简介
- 项目功能：上传图片，识别并返回图片中的字母，并将结果持久化到数据库中（使用联合唯一索引：图片 md5、图片文件大小），数据库默认为 sqlite，可以选配为 mysql
- OCR 技术选型： 选择最快速简单的 tesseract
- 关键依赖：
  - Python：3.8.2
  - Django：3.2.6
  - django rest framework：3.12.4
  - pytesseract：0.3.8
- Dockerfile： docker 镜像分层有助于加快代码构建和发布速度，因此项目提供了 DockerfileBaseImage 以及 Dockerfile 两个文件。
  - DockerfileBaseImage：用于构建基础镜像，供后续构建代码镜像使用，主要是预先安装系统和项目依赖项
  - Dockerfile：以上面构建的基础镜像为基础构建代码发布镜像，只是简单地代码拷贝到镜像中，因此构建速度会非常快
  
### 测试
`python manage.py test`

### 接口文档
- 项目里接口文档采用 swagger，使用的 python 库是 [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)
- 项目 swagger url 地址： http://127.0.0.1:8000/swagger/
- 下面这个 markdown 接口文档是使用工具通过 swagger 数据 url 生成的，可读性一般，建议将接口导入到 api fox 之类的工具中提高可读性
    - [接口文档](docs/swagger.md)

### 部署
提供基础的 docker 镜像快速启动项目和环境变量说明：
[部署文档](docs/deploy.md)
