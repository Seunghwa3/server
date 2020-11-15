from rest_framework import serializers
from polls.models import *

class ReceiveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Receive
		fields = '__all__'

class SendSerializer(serializers.ModelSerializer):
	receive = models.ForeignKey(Receive, on_delete=models.CASCADE, blank=True)
	
	class Meta:
		model = Send
		fields = ['receive', 'product_name', 'price', 'detail']