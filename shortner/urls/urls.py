from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_url, name='create_url'),
    path('<str:uuid>', views.redirect_url, name='redirect_url'),
]