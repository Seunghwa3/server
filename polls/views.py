import json

import os
import csv
import pandas as pd
from surprise import SVDpp
from surprise import Dataset
from surprise import Reader
from surprise import dump
from surprise.model_selection import train_test_split

from polls.models import Send, Receive
from polls.serializer import ReceiveSerializer, SendSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PostList(APIView):

    def get(self, request, format=None):
        area = request.GET['area']
        user_id = request.GET['user_id']
        
        def svd(userID, nowarea) :
            algo = SVDpp()
            algo = SVDpp(n_factors=100, n_epochs=15)
            # 3. train model 저장
            file_name=os.path.expanduser('./dump')
            #dump.dump(file_name, algo=algo) # 한번 학습하고 여기는 주석처리
            _, algo=dump.load(file_name)


            Area=pd.read_csv('./area.csv') ## { 상품아이디(학습데이터), area, 상품ID }

            #nowarea="C"
            #user=str("A2CX7LUOHB2NDG") # usre ID 받아오기
            neww=area[Area['area']==nowarea]['productID'].tolist() # 구역 받아오기
            predictions=[algo.predict(str(user_id), str(productID)) for productID in neww] # 예측
            ######
            def sortkey_est(pred):
            return pred.est
            predictions.sort(key=sortkey_est, reverse=True)
            #print(predictions)
            top_product_id = [int(pred.iid) for pred in predictions]
            top_product_id=top_product_id[:5]
            return top_product_id
            #fortest
        tmp=svdclass.svd("A2CX7LUOHB2NDG", 'A')
        # return vlaue :
        #[594450209, 321732944, 594287995, 594033926, 594033934, 594296420, 594033896, 511189877, 594450705, 594451647, 594477670, 594017343, 594017580, 594202442, 594481813, 558835155, 594478162, 594012015, 439886341, 528881469]
        print(tmp[0])

        send = Send.objects.all().filter(product_id=top_product_id)
        serializer = SendSerializer(send, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

