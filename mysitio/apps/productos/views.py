from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
from apps.productos.forms import ProductoForm
from apps.productos.models import Productos
# Create your views here.
class ProductoCrear(CreateView):
	"""vistas basadas en clases"""
	model = Productos
	form_class = ProductoForm
	template_name = 'sistema/productos_form.html'
	success_url = reverse_lazy('productos_lista')

class ProductoList(ListView):
	"""docstring for """
	model = Productos
	template_name = 'sistema/productos_lista.html'
	paginate_by = 5

class ProductoListS(ListView):
	model = Productos
	template_name = 'sistema/productos_lista.html'
	paginate_by = 5


	def get_queryset(self):
		filter_val = self.request.GET.get('filter')
		if filter_val == '':
			new_context = Productos.objects.all()
			
		else:
			new_context = Productos.objects.filter(nom_producto=filter_val) | Productos.objects.filter(clave_producto=filter_val)
			print(new_context)
		return new_context
class ProductoDelete(DeleteView):
	""""""
	model = Productos
	template_name = 'sistema/productos_delete.html'
	success_url = reverse_lazy('productos_lista')

class ProductoUpdate(UpdateView):
	
	model = Productos
	form_class = ProductoForm
	template_name = 'sistema/producto_editar.html'
	success_url = reverse_lazy('productos_lista')