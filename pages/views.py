from django.shortcuts import render
from .models import Page 

# Create your views here.
def page(request, slug): #agregamos el slug al path de esta funcion 
        page = Page.objects.get(slug = slug) #hacemos consulta en la base de datos

        return render(request, "pages/page.html",
        {
            
            "page": page
        })