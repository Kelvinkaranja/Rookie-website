from django.urls import path
from . import views

urlpatterns= [
	path('',views.view11,name='view11'),
	path('auth',views.auth,name='auth'),


]