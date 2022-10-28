from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view11(response):
	return render(response,'main/base.html',{})

def auth(response):
	return render(response,'main/auth.html',{})