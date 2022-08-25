from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.hello, name="hello"),  
    path('testemail/', views.sendEmail, name="testemail") 
]