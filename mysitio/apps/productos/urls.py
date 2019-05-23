from django.urls import path,include
 
from apps.productos.views import ProductoCrear, ProductoList, ProductoDelete


urlpatterns = [

    path('nuevo', ProductoCrear.as_view(), name='producto_nuevo'),
    path('lista', ProductoList.as_view(), name='productos_lista'),
    path('eliminar/<int:pk>/', ProductoDelete.as_view(), name='productos_eliminar'),


   ]