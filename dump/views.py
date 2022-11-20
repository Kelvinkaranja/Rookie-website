from django.shortcuts import render
from .forms import Registrationform
from django.http import HttpResponse,HttpResponseRedirect
from .models import Login, Contents
# Create your views here.

#Create Home View.
def home(response):
	return render(response,'dump/top.html',{})

#Create Login View.
def login(response):
	return render(response,'dump/list.html',{})

#Create Registrartion View.
def registration(response):
	#Save your form data upon validation
	if response.POST:
		form=Registrationform(response.POST)
		if form.is_valid():
			form.save()
			#Redirect to the welcome page
		return HttpResponseRedirect('dump/welcome.html',{'user':username})
	return render(response,'dump/regform.html',{"form":Registrationform})

#Create Welcome View.
def welcome(response):
	form=Registrationform(response.POST)
	form.save()
	#Assign username for use in html dictionary
	username = form.cleaned_data.get("username")
	usernames=Login.objects.all()
	for a in usernames:
		user=(a.username)
		users=user.upper()
	log=Login(username)
	return render(response, 'dump/welcome.html',{'user':users})

