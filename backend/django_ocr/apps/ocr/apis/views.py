import hashlib

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from rest_framework import viewsets, mixins, parsers
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from contrib.drf.viewsets import SerializerMixin
from ocr.apis.serializers import (
    OcrParseLetterReqSer,
    OcrRecordDisplaySer,
)
from ocr.models import OcrRecord
from services.ocr.tesseract import TesseractOcrService
from .filters import OcrRecordFilter
from .schemas import OcrRecordSchema


class OcrRecordViewSet(
    SerializerMixin,
    # mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_classes = {
        'default': OcrRecordDisplaySer,
        'parse_letter': OcrParseLetterReqSer,
    }
    filterset_class = OcrRecordFilter
    queryset = OcrRecord.objects.all()
    search_fields = []
    ordering = '-id'
    form_actions = {'parse_letter'}

    def get_parsers(self):
        if getattr(self, 'action', None) in self.form_actions:
            return [parsers.FormParser(), parsers.MultiPartParser()]
        return super().get_parsers()

    @OcrRecordSchema.retrieve()
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

    @OcrRecordSchema.list()
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    @OcrRecordSchema.parse_letter()
    @action(detail=False, methods=['POST'], url_name='parse_letter')
    def parse_letter(self, *args, **kwargs):
        req_serializer: OcrParseLetterReqSer = self.get_request_serializer()
        image: InMemoryUploadedFile = req_serializer.validated_data['image']

        md5 = hashlib.md5()
        for chunk in image.chunks():
            md5.update(chunk)
        image_md5 = md5.hexdigest().lower()
        image_size = image.size

        ocr_record: OcrRecord = OcrRecord.objects.filter(image_md5=image_md5, image_size=image_size).first()
        if ocr_record:
            return Response({'content': ocr_record.content})

        letter_list, err = TesseractOcrService.parse_letter(Image.open(image))
        if err:
            raise APIException(f'识别失败:{err}')

        ocr_record = OcrRecord.objects.create(
            image_md5=image_md5,
            image_size=image_size,
            content=letter_list,
        )
        return Response({'content': ocr_record.content})
