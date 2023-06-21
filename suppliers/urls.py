from django.contrib import admin
from django.urls import path
from suppliers.views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home.index, name='home'),
        
]