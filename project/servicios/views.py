from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Cliente, Pedido, Producto
from .forms import ClienteForm, PedidoForm, ProductoForm
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import CustomUserCreationForm, UserProfileForm

def index(request):
    return render(request, "servicios/index.html")

def cliente_list(request):
    q = request.GET.get('q')
    if q:
        query = Cliente.objects.filter(apellido__icontains=q)
    else:
        query = Cliente.objects.all()
    context = {'object_list': query}
    return render(request, "servicios/cliente_list.html", context)

class ClienteList(ListView):
    model = Cliente
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Cliente.objects.filter(apellido__icontains=q)
        return queryset

def producto_list(request):
    q = request.GET.get('q')
    if q:
        query = Producto.objects.filter(nombre__icontains=q)
    else:
        query = Producto.objects.all()
    context = {'object_list': query}
    return render(request, "servicios/producto_list.html", context)

class ProductoList(ListView):
    model = Producto
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Producto.objects.filter(nombre__icontains=q)
        return queryset

def pedido_list(request):
    q = request.GET.get('q')
    if q:
        query = Pedido.objects.filter(cliente__icontains=q)
    else:
        query = Pedido.objects.all()
    context = {'object_list': query}
    return render(request, "servicios/pedido_list.html", context)

class PedidoList(ListView):
    model = Pedido
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Pedido.objects.filter(cliente__icontains=q)
        return queryset

def cliente_create(request):
    if request.method == "GET":
        form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    return render(request, "servicios/cliente_create.html", {"form": form})

def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedido_list")
    return render(request, "servicios/pedido_create.html", {"form": form})

def producto_create(request):
    if request.method == "GET":
        form = ProductoForm()
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto_list")
    return render(request, "servicios/producto_create.html", {"form": form})

def producto_detail(request, pk: int):
    query = Producto.objects.get(id=pk)
    context = {'object': query}
    return render(request, "servicios/producto_detalles.html", context)

def producto_update(request, pk: int):
    query = Producto.objects.get(id=pk)
    if request.method == "GET":
        form = ProductoForm(instance=query)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto_list")
    return render(request, "servicios/producto_create.html", {"form": form})

def producto_delete(request, pk: int):
    query = Producto.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("producto_list")
    return render(request, "servicios/producto_confirm_delete.html", {'object': query})

class Registro(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registro.html"
    success_url = reverse_lazy('login')

class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "profile.html"
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user