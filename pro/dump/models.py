from django.db import models

# Create your models here.
class Login(models.Model):
	username=models.CharField(max_length=100)

	def __str__(self):
		return self.username

class Contents(models.Model):
	table=models.ForeignKey(Login, on_delete=models.CASCADE)
	usernames=models.CharField(max_length=100)
	password=models.CharField(max_length=200)
	online=models.BooleanField()

	def __str__(self):
		return self.usernames