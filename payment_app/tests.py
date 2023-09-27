from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from payment_app.models import Payment
from settlement_app.models import Settlement
from decimal import Decimal
from rest_framework.test import APIRequestFactory
from unittest.mock import patch
import unittest
class CreatePaymentTestCase(APITestCase):

    def test_create_payment(self):
        url = reverse('create_payment')
        data = {"amount": "800.00",  "sender_id": "10",  "recipient_id": "8"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.get().amount, Decimal('800'))
        self.assertEqual(Payment.objects.get().sender_id, "10")
        self.assertEqual(Payment.objects.get().recipient_id, "8")

    def test_get_payment_details(self):
        Payment.objects.create(amount=Decimal("100"),sender_id="1",recipient_id="1")
        # new_url = f'api/payments/1/'
        # get_response = self.client.get(new_url)
        factory = APIRequestFactory()
        response = factory.put(f'/api/payments/1/', {'amount': '200'})
        self.assertEqual(response.method, "PUT")
        # self.assertEqual(response.POST.get("amount",0), Payment.objects.get().amount)
        # self.assertEqual(response.status_code,status.HTTP_200_OK)

class GetPaymentTestCase(unittest.TestCase):
    # @patch(payment)
    def test_get_payment_details(self):
        pass


    
        