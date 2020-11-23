from rest_framework import serializers
from polls.models import *

class ReceiveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Receive
		fields = ['area', 'age', 'gender']

class SendSerializer(serializers.ModelSerializer):
	class Meta:
		model = Send
		fields = ['product_id', 'product_name', 'price', 'detail','image_addr']