from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name= 'inicio'),

    path('cliente/', cliente, name = 'cliente'),
    path('Top/', top, name = 'top'),
    path('camisas/', camisas, name = 'camisas'),
    path('short/', short, name = 'short'),
    path('camperas/', camperas, name = 'camperas'),
    path('championes/', championes, name = 'championes'),

    path('cliente_form/', clienteForm, name="cliente_form"),
    path('cliente_form2/', clienteForm2, name="cliente_form2"),

    path('pantalones/', pantalones, name = 'pantalones'),
    path('update_pantalones/<id_pantalones>/', updatePantalones, name = "update_pantalones"),
    path('delete_pantalones/<id_pantalones>/', deletePantalones, name = "delete_pantalones"),
    

    path('campera/list', CamperasList.as_view(), name='Camperas')



]
   