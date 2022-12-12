from . import views
from django.urls import path
urlpatterns=[
path('home',views.home,name='home'),
path('login',views.login,name='login'),
path('registration',views.registration,name='registration'),
path('welcome',views.welcome,name='welcome'),

]