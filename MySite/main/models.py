from django.db import models

# Create your models here.
class Table1(models.Model):
	name=models.CharField(max_length=300)
	

	def __str__(self):
		return self.name 

class Cols(models.Model):
	table=models.ForeignKey(Table1, on_delete=models.CASCADE)
	first_name=models.CharField(max_length=200)
	balance=models.IntegerField()
	active=models.BooleanField()

	def __str__ (self):
		if self.active==True:
			activity='TRUE'
		else:
			activity='FALSE'
		return f'{self.first_name}  -  {self.balance}  -  {activity}'