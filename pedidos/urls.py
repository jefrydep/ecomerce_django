from django.urls import path

from  pedidos.views import *

urlpatterns = [
    
    path('', pedidos, name="Blog"),
    


]