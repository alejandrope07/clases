from django.urls import path,include
 
from apps.ventas.views import VentasCrear, VentasList, VentasDelete


urlpatterns = [

    path('nuevo', VentasCrear.as_view(), name='ventas_nuevo'),
    path('lista', VentasList.as_view(), name='ventas_lista'),
    path('eliminar/<int:pk>/', VentasDelete.as_view(), name='ventas_eliminar'),


   ]