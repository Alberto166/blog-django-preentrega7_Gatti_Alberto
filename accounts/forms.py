from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

# Formulario para el Alta / Registro de un nuevo usuario
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Ingresá una dirección de email válida.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

# Formulario para actualizar el Perfil y datos del Usuario
class EditarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label="Nombre")
    last_name = forms.CharField(max_length=30, required=False, label="Apellido")
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = Perfil
        fields = ['biografia', 'link_web', 'avatar']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        perfil = super().save(commit=False)
        user = perfil.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            perfil.save()
        return perfil
