import json

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from polls.models import Send, Receive
from polls.serializer import ReceiveSerializer, SendSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def item_list(request):
	print(request)
	if request.method == 'GET':
		print('get')

		area = self.request.queryset.get('area')
    	age= self.request.queryset.get('age')
    	gender = self.request.queryset.get('gender')
		
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

