# Generated by Django 3.2.6 on 2021-08-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OcrRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
                ('image_md5', models.CharField(help_text='长度为 32 的小写字母、数字', max_length=32, verbose_name='图片的md5')),
                ('image_size', models.PositiveBigIntegerField(verbose_name='图片的大小')),
                ('content', models.JSONField(verbose_name='识别结果')),
            ],
            options={
                'verbose_name': 'ocr 记录',
                'verbose_name_plural': 'ocr 记录',
                'unique_together': {('image_md5', 'image_size')},
            },
        ),
    ]
