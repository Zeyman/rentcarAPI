from django.db import models

# Create your models here.

class Car(models.Model):
	name = models.CharField(max_length=40)
	year = models.IntegerField()
	pic = models.ImageField(upload_to='media/carphotos', default='media/carphotos.error.jpg') 



class Elan(models.Model):
	name = models.CharField(max_length=40)
	year = models.IntegerField()
	price_azn = models.IntegerField()
	

