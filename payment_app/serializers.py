from rest_framework import serializers
from payment_app.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment 
        fields = ['recipient_id','sender_id','amount']

class PaymentAllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment 
        fields = "__all__"

class PaymentAmountDataSerializer(serializers.ModelSerializer):
    class Meta:
            model = Payment 
            fields = ["amount"]

