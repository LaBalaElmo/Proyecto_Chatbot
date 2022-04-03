from django.urls import re_path
from chatbot import views 

urlpatterns = [ 
    re_path('create', views.create),
    re_path('chat', views.chat),
    re_path('hola', views.prueba),
]