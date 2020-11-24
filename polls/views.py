import json

from polls.models import Send, Receive
from polls.serializer import ReceiveSerializer, SendSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from polls.svd_recommend2 import svdclass

# Create your views here.

class PostList(APIView):

    def get(self, request, format=None):
        area = request.GET['area']
        user_id = request.GET['user_id']
        tmp = svdclass.svd(user_id, area)
        for i in tmp :
            product_id = i
            send = Send.objects.all().filter(product_id=product_id)
        serializer = SendSerializer(send, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

