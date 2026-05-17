
from django.contrib import admin
from django.urls import path, include
from urlshort import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('<str:short_url>/', views.redirect_url, name="redirect_url"),
]
