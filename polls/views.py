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
"""
@api_view(['GET', 'POST'])
def item_list(request):
	print(request)
	if request.method == 'GET':
		print('get')

		area = self.request.query_params.get('area')
    	age= self.request.query_params.get('age')
    	gender = self.request.query_params.get('gender')
		print(gender)
		quaryset = Receive.objects.all()
		serializer = ReceiveSerializer(quaryset, many=True)
		return JsonResponse(serializer.data, safe=False)
	
	elif request.method == 'POST':
		print('post')
		data = JSONParser().parse(request)
		serializer = SendSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
"""

class SnippetList(APIView):

    def get(self, request, format=None):
        receive = Receive.objects.all()
        serializer = ReceiveSerializer(receive, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)