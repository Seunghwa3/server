import json

from polls.models import Send, Receive
from polls.serializer import ReceiveSerializer, SendSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PostList(APIView):
        
    def get(self, request, format=None):
        receive = Receive.GET.request.GET['area']
        send = Send.objects.all()
        serializer = SendSerializer(send, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReceiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

