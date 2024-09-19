from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Pedido, Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label="Seleccione un cliente")
    producto = forms.ModelChoiceField(queryset=Producto.objects.filter(stock=True), empty_label="Seleccione un producto")
    class Meta:
        model = Pedido
        fields = "__all__"
        widgets = {
            "fecha_entrega": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')