from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pymongo
from payment_app.models import Payment
from settlement_app.models import Settlement
from payment_app.views import set_key,get_key,delete_key
from django.forms.models import model_to_dict
import uuid

# Mongodb

CONN_STR = "mongodb+srv://test_user:BydxRm6az8YZ1lHi@cluster0.nfztvrp.mongodb.net/"

def mongodb_connection(conn_str):
    client = pymongo.MongoClient(conn_str)
    return client

def mongodb_create_db_collection(conn_str):
    client = mongodb_connection(conn_str)
    db = client['settlement_data']
    collections = db['settlement_records']

@csrf_exempt
@api_view(['POST'])
def create_settlements(request):
    if request.method == 'POST':
        data = request.data
        payment_ids = data.get('payment_ids',[])
        settled_amount = data.get('settled_amount', 0)
        data_to_save = {"payment_data" : [], "settlement_data" : [], "settled_amount" : settled_amount, "settlement_id":None}
        if payment_ids and settled_amount:
            for pay_id in payment_ids:
                try:
                    pay_id = int(pay_id)
                    payment_obj = Payment.objects.get(id=pay_id)
                    payment_obj.status = "COMPLETED"
                    deimal_obj_amount = payment_obj.amount 
                    payment_obj.amount = float(deimal_obj_amount)
                    pay_data = model_to_dict(payment_obj)
                    set_key(pay_id,pay_data)
                    data_to_save["payment_data"].append(pay_data)
                    # Once the payment_status is completed, we can use kafka to send the notifications to sender and receiver
                    settlement_obj = Settlement.objects.create(payment = payment_obj)
                    settlement_id = str(uuid.uuid4())
                    data_to_save["settlement_id"] = settlement_id
                    settlement_data = model_to_dict(settlement_obj)
                    data_to_save["settlement_data"].append(settlement_data)
                except Exception as e:
                    print(f"API create_settlements failed due to {e}")
        if data_to_save.get("payment_data",[]) and data_to_save.get("settlement_data",[]):
            try:
                client = mongodb_connection(CONN_STR)
                db = client['settlement_data']
                collections = db['settlement_records']
                collections.insert_one(data_to_save)
                client.close()
                try:
                    set_key(settlement_id,data_to_save)
                except Exception as e:
                    print(f"Failed to save the data into redis : {e}")
                return Response(f"Data Saved to mongodb : {data_to_save}", status=status.HTTP_200_OK)
            except Exception as e:
                print(f"Failed in pushing data to MongoDB : {e} ")
                return Response("Failed because of bad request", status=status.HTTP_400_BAD_REQUEST)
        return Response("API create_settlements failed because of bad request", status=status.HTTP_400_BAD_REQUEST)
    return Response("API create_settlements failed because of bad request", status=status.HTTP_400_BAD_REQUEST)
                    
@csrf_exempt
@api_view(['GET'])
def retrieve_settlement(request,settlement_id):
    res = get_key(settlement_id)
    if res:
        result = []
        result.append(res)
        print(f"Data fetched from redis : {result}")
        return Response(f"Settlement ID : {settlement_id} and Data : {result}", status=status.HTTP_200_OK)
    else:
        try:
            client = mongodb_connection(CONN_STR)
            db = client['settlement_data']
            collections = db['settlement_records']
            query = {"settlement_id": settlement_id}
            matching_documents = collections.find(query)
            result = []
            for m in matching_documents:
                result.append(m)
            client.close()
            return Response(f"Settlement ID : {settlement_id} and Data : {result}", status=status.HTTP_200_OK)
        except Exception as e:
            print(f"API retrieve_settlement failed to get the data from MongoDB : {e}")
    return Response("API retrieve_settlement failed because of bad request", status=status.HTTP_400_BAD_REQUEST)

