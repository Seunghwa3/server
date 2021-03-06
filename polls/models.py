from django.db import models

# Create your models here.

class Receive(models.Model):
	area         = models.CharField(max_length=10)
	user_id      = models.CharField(max_length=30)

	def __str__(self):
		return self.area

class Send(models.Model):
	product_id   = models.IntegerField(default=0)
	product_name = models.CharField(max_length=100)
	price        = models.IntegerField(default=0)
	detail       = models.CharField(max_length=300)
	image_addr   = models.ImageField(upload_to='images/', null=True, blank=True)

	def __str__(self):
		return self.product_name