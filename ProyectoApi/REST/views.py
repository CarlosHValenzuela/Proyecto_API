from typing import Any
from django import http
from django.shortcuts import render
from django.views import View
from .models import Producto, Boleta, Registro
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.shortcuts import redirect


def home(request):
    productosListados = Producto.objects.all()
    return render(request, "index.html", {"productos": productosListados})

def detalle(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, "detalle.html", {"producto": producto})

def comprarVenta(request):
        id = request.POST['txtId']
        title = request.POST['txtTitle']
        price = request.POST['txtPrice']
        stock = request.POST['txtStock']
        cantidad = request.POST['txtCantidad']

        producto = Producto.objects.get(id=id)
        producto.title = title
        producto.price = price
        producto.stock -= int(cantidad)
        producto.save()
        return redirect('/')

def registroPagina(request):
    return render(request, "registro.html")

def registrarVenta(request):
        id = request.POST['txtId']
        rut = request.POST['txtRut']
        address = request.POST['txtAddress']
        email = request.POST['txtEmail']

        boleta = Boleta.objects.create(
            id=id, rut=rut, address=address, email=email
        )

        return redirect('/')
 
# def registrar_venta(request, id):
            


#---------------------------API REST-------------------------------------------
class LibroView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #Todos los productos
    def get(self, request):
        libros=list(Producto.objects.values())
        if len(libros)>0:
            datos={'message': "Listado",'libros': libros}
        else:
            datos={'message': "Libro no encontrado"}
        return JsonResponse(datos)

    #Deberia restar el producto
def compras(self, request, id):
    jd = json.loads(request.body)
    libros = list(Producto.objects.filter(id=id).values())
    if len(libros)>0:
        libro=Producto.objects.get(id=id)
        libro.stock = libro.stock - jd['stock']
        libro.save()
        datos=({'mensaje': 'Compra realizada'})
    else:
        datos={'message': "Libro no encontrado"}
        return JsonResponse(datos)

    #Lista segun el ID
    def get(self, request, id=0):
        if (id>0):
            libros= list(Producto.objects.filter(id=id).values())
            if len(libros)> 0:
                libro = libros[0]
                datos = {'message': 'Libro', 'libro': libro}
            else:
                datos = {'message': 'Libro no encontrado......'}
            return JsonResponse(datos)
        else:
            libros = list(Producto.objects.values())
            if len(libros)>0:
                datos = {'message': 'Success', 'libro': libros}
            else:
                datos = {'message': 'Libro no encontrado.....'}
            return JsonResponse(datos)