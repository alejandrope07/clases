from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
from apps.ventas.forms import VentasForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.ventas.models import Ventas
# Create your views here.
class VentasCrear(CreateView):
	"""vistas basadas en clases"""
	model = Ventas
	form_class = VentasForm
	template_name = 'sistema/ventas_form.html'
	success_url = reverse_lazy('ventas_lista')

class VentasList(ListView):
	"""docstring for"""
	model = Ventas
	template_name = 'sistema/ventas_lista.html'
	paginate_by = 5

class VentasDelete(DeleteView):
	"""docstring for """
	model = Ventas
	template_name = 'sistema/ventas_delete.html'
	success_url = reverse_lazy('ventas_lista')