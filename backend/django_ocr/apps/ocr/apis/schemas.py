from drf_yasg.utils import swagger_auto_schema

from ocr.apis.serializers import OcrParseLetterResSer


class OcrRecordSchema:
    @classmethod
    def parse_letter(cls):
        return swagger_auto_schema(
            operation_summary='解析图片中的字母',
            responses={'200': OcrParseLetterResSer()},
        )
