import unittest
from PIL import Image
from img_api.models import MImg
from django.test.client import RequestFactory
from . import views


class MImgTest(unittest.TestCase):

    def setUp(self) -> None:
        self.request = RequestFactory()

    # --------- Use case 1 ----------------
    # Scenario 1
    def getTest1(self):
        MImg.objects.create(path='media/images/blue.jpg', content=Image, name='blue')
        request = self.request.get('image/blue')
        response = views.ImgHandler.as_view(request)
        self.assertEqual(response.status_code, 200)

    # Scenario 2
    def getTest2(self):
        request = self.request.get('image/blue')
        response = views.ImgHandler.as_view(request)
        self.assertEqual(response.status_code, 404)

    # --------- Use case 2 ----------------
    # Scenario 1
    def postTest(self):
        request = self.request.post('image/blue')
        response = views.ImgHandler.as_view(request)
        self.assertEqual(response.status_code, 200)

    # Scenario 2
    def putTest(self):
        request = self.request.put('image/blue')
        response = views.ImgHandler.as_view(request)
        self.assertEqual(response.status_code, 200)


