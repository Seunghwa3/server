import json

from polls.models import Send, Receive
from polls.serializer import ReceiveSerializer, SendSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SnippetList(APIView):

    def get(self, request, format=None):
        send = Send.objects.all().filter(product_name='A')
        serializer = SendSerializer(send, many=True)
        return Response(serializer.data)