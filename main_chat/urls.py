from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='home'),
    path('chat', views.chat,name='chat'),
    path('cinema',views.cinema,name='cinema'),
    path('music', views.music,name='music')
]
