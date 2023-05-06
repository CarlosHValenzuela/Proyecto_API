from django.urls import path
from .views import LibroView 

urlpatterns=[
    path('libros/', LibroView.as_view(), name='libros_list'),
    path('libros/<int:id>',LibroView.as_view(),name='libros_process')
    ]