import os

from django.conf import settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class OcrRecordViewSetTestCase(APITestCase):
    def test_parse_letter(self):
        url = reverse('api_routers:ocr_record-parse_letter')
        test_image_file_path = os.path.join(settings.FIXTURE_DIR, 'ocr/hello_word.png')
        with open(test_image_file_path, 'rb') as image:
            data = {
                'image': image
            }
            resp = self.client.post(url, data=data, format='multipart')
            self.assertEqual(resp.status_code, status.HTTP_200_OK)
            self.assertTrue('content' in resp.data)
            self.assertTrue(len(resp.data['content']) > 0)
