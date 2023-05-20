from django.shortcuts import render
from blog.models import *

# Create your views here.

def blog(request):

    posts= Post.objects.all()

    return render(request,"blog/blog.html", {"posts":posts})


def categoria(request, categoria_id):

    categoria= Categoria.objects.get(id=categoria_id) #obtener el id de la categoria many to many 
    posts= Post.objects.filter(categoria=categoria) #dividir los post por categoria

    return render(request, "blog/categoria.html", {"categoria":categoria, "posts":posts})






   
