from django.shortcuts import render
import requests

#todo es una vista basada en funcion que va a renderizar la plantilla
def index(request):
    template_name="index.html"
    response = requests.get('http://127.0.0.1:7000/api/productsall/')
    productos = response.json
    context = {
        "productos":productos
    }
    print(context)
    return render(request,template_name,context)
