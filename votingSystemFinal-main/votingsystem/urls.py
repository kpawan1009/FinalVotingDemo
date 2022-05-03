
from django.contrib import admin
from django.urls import path,include
import web3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.url')),
]
