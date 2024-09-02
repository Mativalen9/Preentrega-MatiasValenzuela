from django import forms

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
        widgets = {"fecha entrega": forms.DateTimeInput(attrs={"type": "datetime-local"})}
