from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class TestFileUpload(APITestCase):
    def test_file_is_accepted(self):
        filename = 'deals'
        with open('api/tests/{}.csv'.format(filename), 'r') as file:
            url_path = reverse('api:deals-import-deals-file')
            response = self.client.post(
                url_path,
                {"file": file},
            )
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            self.assertEqual('Файл был обработан без ошибок.',
                             response.data['detail'])

    def test_file_with_invalid_name_is_declined(self):
        filename = 'deals2'
        with open('api/tests/{}.csv'.format(filename), 'r') as file:
            url_path = reverse('api:deals-import-deals-file')
            response = self.client.post(
                url_path,
                {"file": file},
            )
            self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
            self.assertEqual('Прикрепите файл deals.csv.',
                             response.data['detail'])
