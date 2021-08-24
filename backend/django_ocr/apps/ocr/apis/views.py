from rest_framework import viewsets, mixins, parsers
from rest_framework.decorators import action
from rest_framework.response import Response

from contrib.drf.viewsets import SerializerMixin
from ocr.apis.serializers import OcrParseLetterReqSer
from .schemas import OcrRecordSchema


class OcrRecordViewSet(
    SerializerMixin,
    # mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_classes = {
        'parse_letter': OcrParseLetterReqSer,
    }
    form_actions = {'parse_letter'}

    def get_parsers(self):
        if getattr(self, 'action', None) in self.form_actions:
            return [parsers.FormParser(), parsers.MultiPartParser()]
        return super().get_parsers()

    @OcrRecordSchema.parse_letter()
    @action(detail=False, methods=['POST'])
    def parse_letter(self, *args, **kwargs):
        req_serializer: OcrParseLetterReqSer = self.get_request_serializer()
        image = req_serializer.validated_data['image']
        return Response()
