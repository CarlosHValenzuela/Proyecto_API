from django.urls import path
from .views import LibroView, home, detalle, comprarVenta, registrarVenta

urlpatterns=[
    path('libros/', LibroView.as_view(), name='libros_list'), #API
    path('libros/<int:id>',LibroView.as_view(),name='libros_process'),#API


    path('registrarVenta/', registrarVenta),
    path('', home),#PAGINA
    path('detalle/comprarVenta/', comprarVenta),
    path('detalle/<id>', detalle)#PAGINA
    ]