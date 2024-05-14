from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


def home(request):
    return render(request, "producto/index.html")


# *** PRODUCTOCATEOGORIA

# LIST
# def productocategoria_list(request):
#     consulta = request.GET.get("consulta", None)
#     if consulta:
#         print(consulta)
#         query = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
#     else:
#         query = models.ProductoCategoria.objects.all()
#     context = {"productos": query}
#     return render(request, "producto/productocategoria_list.html", context)


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria

    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     consulta = self.request.GET.get("consulta")
    #     if consulta:
    #         queryset = queryset.filter(Q(nombre__icontains=consulta) | Q(descripcion__icontains=consulta))
    #     return queryset


# CREATE
# def productocategoria_create(request):
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect("producto:home")
#     else:  # request.method == "GET"
#         form = forms.ProductoCategoriaForm()
#     return render(request, "producto/productocategoria_create.html", context={"form": form})


class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:home")


# UPDATE
# def productocategoria_update(request, pk: int):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST, instance=query)
#         if form.is_valid:
#             form.save()
#             return redirect("producto:productocategoria_list")
#     else:  # request.method == "GET"
#         form = forms.ProductoCategoriaForm(instance=query)
#     return render(request, "producto/productocategoria_update.html", context={"form": form})


class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


# DETAIL
# def productocategoria_detail(request, pk: int):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     return render(request, "producto/productocategoria_detail.html", {"producto": query})


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    # context_object_name = "producto"


# DELETE
# def productocategoria_delete(request, pk: int):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         query.delete()
#         return redirect("producto:productocategoria_list")
#     return render(request, "producto/productocategoria_delete.html", context={"producto": query})


class ProductoCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.ProductoCategoria
    # template_name = "producto/productocategoria_delete.html"
    success_url = reverse_lazy("producto:productocategoria_list")


# *** PRODUCTO


class ProductoList(ListView):
    model = models.Producto

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list


class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:home")


class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDetail(DetailView):
    model = models.Producto


class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
