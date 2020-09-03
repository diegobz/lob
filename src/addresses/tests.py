from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .models import Address

class TestModel1Api(TestCase):

    fixtures = ['addresses']

    def setUp(self):
        self.client = APIClient()

    def test_list(self):
        response = self.client.get(reverse('address-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        obj = Address.objects.all()[0]
        response = self.client.get(reverse('address-detail', args=[obj.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search(self):
        response = self.client.get(
            reverse('address-list') + '?search=1600')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_post(self):
        data = {
            "line1": "354 Partridge Ave",
            "city": "Menlo Park",
            "state": "CA",
            "zipcode": "94025"
        }
        response = self.client.post(reverse('address-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patch(self):
        data = {
            "zipcode": "94025"
        }
        obj = Address.objects.all()[0]
        response = self.client.patch(reverse('address-detail', args=[obj.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete(self):
        obj = Address.objects.all()[0]
        response = self.client.delete(reverse('address-detail', args=[obj.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
