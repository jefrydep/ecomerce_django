#from .carro import Carro
from django.contrib import messages



def importe_total_carro(request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items(): 
            total=total+float(value['precio'])
    else:
        messages.error(request, "Para ver carrito")
            
    return {'importe_total_carro':total}   
        
