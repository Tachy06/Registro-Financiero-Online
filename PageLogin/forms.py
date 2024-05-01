from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control userRegister'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control passwordRegister'}))

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Primer nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Apellidos', widget=forms.TextInput(attrs={'class': 'form-control'}))
    usuario  = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control userRegister'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control emailRegister'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control passwordRegister'}))
    confirm_password = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control passwordRegister'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return cleaned_data
    
class RegisterCardForm(forms.Form):
    card = forms.CharField(label="Número de tarjeta",required=True, max_length=16, min_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(label='Fecha de vencimiento', required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    cvv = forms.CharField(label="CVV", required=True, max_length=3, min_length=3, widget=forms.NumberInput(attrs={'class': 'form-control'}))