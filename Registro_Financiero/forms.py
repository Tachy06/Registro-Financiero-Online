from django import forms

class RegistroFinance(forms.Form):
    PAYMENT_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
    ]
    tipo = forms.ChoiceField(label='Tipo de gasto', choices=PAYMENT_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'radio'}))
    cantidad = forms.CharField(label='Cantidad gastado', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(label='Fecha cuando lo gastaste', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))