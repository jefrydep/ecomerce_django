
from django.urls import path

from servicios.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', servicios, name="Servicios"),
    
    

]






