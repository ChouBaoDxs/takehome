from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ocr.apis.views import OcrRecordViewSet

defalt_router = SimpleRouter()
defalt_router.register('ocr_record', OcrRecordViewSet, basename='ocr_record')


app_name = 'api_routers'
urlpatterns = [
    path('', include(defalt_router.urls)),
]
