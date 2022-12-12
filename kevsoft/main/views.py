from django.shortcuts import render
from django.http import HttpResponse
# Create your views here


def index(respose):
	return HttpResponse('<h1>KEVSOFT TECH <h1>')
def view1(respose):
	return HttpResponse('<h1>KEVSOFT TECH view1 <h1>')
