from django import forms

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from apps.productos.models import Productos

from django.contrib.admin import widgets


class ProductoForm(forms.ModelForm):
	"""docstring for """
	class Meta:
		model = Productos

		fields = [
			'clave_producto',
			'cantidad',
			'nom_producto',
			'descripcion',
			'precio',


		]
		labels = {
            'clave_producto': 'Clave del producto',
			'cantidad': 'Cantidad',
			'nom_producto': 'Nombre del producto',
			'descripcion': 'Descripción',
			'precio': 'Precio',




		}

		widgets = {
            'clave_producto': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
			'nom_producto': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'precio': forms.TextInput(attrs={'class': 'form-control'}),


		}
