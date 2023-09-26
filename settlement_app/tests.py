from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from payment_app.models import Payment
from settlement_app.models import Settlement
from decimal import Decimal
from rest_framework.test import APIRequestFactory

class CreateSettlementTestCase(APITestCase):

    def test_create_payment(self):
        # url = reverse('create_settlements')
        # data = { "payment_ids": ["17", "18"], "settled_amount": 1250.0 }
        # response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        pass