from django.db import models

# Create your models here.

class Receive(models.Model):
	area         = models.CharField(max_length=10)
	age          = models.IntegerField(default=0)
	gender       = models.CharField(max_length=30)

	def __str__(self):
		return self.area

class Send(models.Model):
	product_name = models.CharField(max_length=100)
	price        = models.IntegerField(default=0)
	detail       = models.CharField(max_length=300)
	image_addr   = models.CharField(max_length=300)

	def __str__(self):
		return self.product_name