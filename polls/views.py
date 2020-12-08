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
        


        send = Send.objects.filter(detail='-')
        serializer = SendSerializer(send, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

