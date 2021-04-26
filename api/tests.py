from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.test import APITestCase


class TestFileUpload(APITestCase):
    def test_file_is_accepted(self):
        filename = "deals"
        with open("api/tests/{}.csv".format(filename), "r") as file:
            url_path = reverse("api:deals-import-deals-file")
            response = self.client.post(
                url_path,
                {"file": file},
            )
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            self.assertEqual(_("Файл был обработан без ошибок."), response.data["detail"])

    def test_invalid_file_name_is_declined(self):
        filename = "deals"
        with open("api/tests/{}.csv".format(filename), "r") as file:
            url_path = reverse("api:deals-import-deals-file")
            response = self.client.post(
                url_path,
                {"file_another_name": file},
            )
            self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
            self.assertEqual(_("Прикрепите файл deals.csv."), response.data["detail"])
