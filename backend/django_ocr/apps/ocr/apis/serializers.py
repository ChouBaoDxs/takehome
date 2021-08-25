from rest_framework import serializers

from ocr.models import OcrRecord


class OcrParseLetterReqSer(serializers.Serializer):
    image = serializers.ImageField()


class OcrParseLetterResSer(serializers.Serializer):
    content = serializers.ListSerializer(
        child=serializers.CharField(help_text='字母', max_length=1, min_length=1),
        help_text='解析图片得到的字母列表',
    )


class OcrRecordDisplaySer(serializers.ModelSerializer):
    content = serializers.ListSerializer(
        child=serializers.CharField(),
        help_text='识别结果',
    )

    class Meta:
        model = OcrRecord
        fields = ['id', 'created_at', 'image_md5', 'image_size', 'content']
