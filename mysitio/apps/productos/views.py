from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
from apps.productos.forms import ProductoForm
from django.contrib.auth.mixins import LoginRequiredMixin
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