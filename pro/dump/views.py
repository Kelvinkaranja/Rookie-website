from django.shortcuts import render
from .forms import Registrationform
from django.http import HttpResponse,HttpResponseRedirect
from .models import Login, Contents
# Create your views here.
def home(response):
	return render(response,'dump/top.html',{})

def login(response):
	return render(response,'dump/list.html',{})

def registration(response):
	if response.POST:
		form=Registrationform(response.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('dump/welcome.html',{'user':username})
	return render(response,'dump/regform.html',{"form":Registrationform})

def welcome(response):
	try:
	    #Registrationform(response.POST):
		form=Registrationform(response.POST)
		form.save()
		username = form.cleaned_data.get("username")
		usernames=Login.objects.all()
		for a in usernames:
			user=(a.username)
			users=user.upper()
		log=Login(username)
		return render(response, 'dump/welcome.html',{'user':users})
	except: 
		#not form.is_valid:
		return render(response,'dump/regform.html',{"form":Registrationform})

