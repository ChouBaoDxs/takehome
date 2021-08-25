FROM choubaodxs/django-ocr-base-image:v1.0

WORKDIR /opt/django_ocr
ADD . .

# 有时候加了新依赖来不及重新构建基础镜像，这里 install 一次
RUN pip install -r requirements.txt --no-cache-dir --timeout 300 -i https://pypi.tuna.tsinghua.edu.cn/simple/

EXPOSE 8000

CMD ["sh", "./entrypoint.sh"]

# build example: docker build -t choubaodxs/django-ocr:v1.0 .