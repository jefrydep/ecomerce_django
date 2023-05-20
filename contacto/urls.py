from django.urls import path

from  contacto.views import *


urlpatterns = [
   
    path('', contacto, name="Contacto"),
    
    


]

