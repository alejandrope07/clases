from django import forms

from django.contrib.admin.widgets import AdminDateWidget
from apps.ventas.models import Ventas

from django.contrib.admin import widgets


class VentasForm(forms.ModelForm):
	"""docstring for """
	class Meta:
		model = Ventas

		fields = [
			'fecha',
			'nom_producto',
			'cantidad',
			'descripcion',
			'precio_uni',
            'precio_t',


		]
		labels = {
			'fecha': 'Fecha',
			'nom_producto': 'Nombre del producto',
			'cantidad': 'Cantidad',
			'descripcion': 'Descripción',
			'precio_uni': 'Precio unitario',
            'precio_t': 'Precio total',




		}

		widgets = {
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
			'nom_producto': forms.TextInput(attrs={'class': 'form-control'}),            
			'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'precio_uni': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_t': forms.TextInput(attrs={'class': 'form-control'}),


		}
