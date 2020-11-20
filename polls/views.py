import json

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from polls.models import Send, Receive
from polls.serializer import ReceiveSerializer, SendSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SnippetList(APIView):

    def get(self, request, format=None):
        receive = Receive.objects.all()
        send = Send.objects.filter(product_name=receive['addr'])
        serializer = SendSerializer(send, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReceiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)