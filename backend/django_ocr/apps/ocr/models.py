from django.db import models

from contrib.models import ReadOnlyModel


class OcrRecord(ReadOnlyModel):
    image_md5 = models.CharField('图片的md5', max_length=32, help_text='长度为 32 的小写字母、数字')
    image_size = models.PositiveBigIntegerField('图片的大小')
    content = models.JSONField('识别结果')

    class Meta:
        verbose_name = verbose_name_plural = 'ocr 记录'
        unique_together = [('image_md5', 'image_size')]  # 简单点，假如文件的 md5 和文件大小相同，视为同一个文件
