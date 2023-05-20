from django.shortcuts import redirect, render

from .forms import *

from  django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto= ContactoForm()
    if request.method== "POST": #si la información viaja por post 
        formulario_contacto= ContactoForm(data=request.POST) #la variable va a capturar la info
        if formulario_contacto.is_valid():
            nombre= request.POST.get("nombre")
            email= request.POST.get("email")
            contenido= request.POST.get("contenido")

            email= EmailMessage("Mensaje desde DJANGO ECOMMERCE",
            "El usuario: {} con la dirección {}, escribe lo siguiente: \n\n {}".format(nombre,email,contenido), 
            "", ["lucasmigliaccio10@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")

            except:
                return redirect("/contacto/?invalido")

            


    return render(request,"contacto/contacto.html", {"miformulario":formulario_contacto})