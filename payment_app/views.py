from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from payment_app.models import Payment
from payment_app.serializers import PaymentSerializer,PaymentAllDataSerializer
from django.core.cache import cache
from django.forms.models import model_to_dict
from decimal import Decimal

CACHE_TTL = 24 * 60 * 60 * 1000
def set_key(key, value, timeout=CACHE_TTL):
    return cache.set(key, value, timeout=timeout)

def get_key(key):
    return cache.get(key)

def delete_key(key):
    return cache.delete(key)

@csrf_exempt
@api_view(['POST'])
def create_payment(request):
    if request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            res = serializer.save()
            model_data = model_to_dict(res)
            # Saving data into the redis:
            set_key(res.id,model_data)
            return Response(model_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def get_payment_details(request,payment_id):
    try:
        payment_obj = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            fetching_from_redis = get_key(payment_id)
            print(f"Fetched from redis")
            print(fetching_from_redis)
            return Response(fetching_from_redis,status = status.HTTP_200_OK)
        except:
            serializer = PaymentAllDataSerializer(payment_obj)
            try:
                set_key(payment_id,serializer.data)
            except Exception as e:
                print(f"Failed to update the data into redis for key: {payment_id}. Error : {e}")
            return Response(serializer.data,status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        print(request.data)
        sender_id = payment_obj.sender_id
        recipient_id = payment_obj.recipient_id
        data = {"amount": Decimal(request.data["amount"]), "sender_id":sender_id, "recipient_id":recipient_id }
        serializer = PaymentAllDataSerializer(payment_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            try:
                set_key(payment_id,serializer.data)
            except Exception as e:
                print(f"Failed to update the data into redis for key: {payment_id}. Error : {e}")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        payment_obj.delete()
        delete_key(payment_id)
        return Response(f"Payment Id: {payment_id} is deleted.",status=status.HTTP_204_NO_CONTENT)



