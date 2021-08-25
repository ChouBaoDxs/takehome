from django_filters import rest_framework as filters

from ocr.models import OcrRecord

class OcrRecordFilter(filters.FilterSet):
    class Meta:
        model = OcrRecord
        fields = {
            'id': ['exact'],
            'image_md5': ['exact'],
            'image_size': ['lte', 'gte'],
            'created_at': ['lte', 'gte'],
        }
