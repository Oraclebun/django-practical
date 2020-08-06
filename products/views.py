from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Product
from .forms import ProductForm, SearchForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Q


# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.template.html', {
        'products': products
    })

@login_required
@permission_required('products.input_product')
def input_product(request):
    if request.method == 'POST':
        input_form = ProductForm(request.POST)

        # if the form is validated
        if input_form.is_valid():
            new_product = input_form.save(commit=False)
            new_product.editor = request.user
            new_product.save()
            messages.success(request,
                             f"New Product {input_form.data['name']}"
                             f"has been entered into the system")
            return redirect(reverse(index))
        else:
            return render(request, 'products/input_product.template.html', {
                          'form': input_form
                          })
    else:
        input_form = ProductForm()
        return render(request, 'products/input_product.template.html', {
            'form': input_form
        })

@login_required
@permission_required('products.update_product')
def update_product(request, product_id):
    product_to_update = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        update_form = ProductForm(request.POST, instance=product_to_update)
        if update_form.is_valid():
            editted_product = update_form.save(commit=False)
            editted_product.editor = request.user
            editted_product.save()
            messages.success(
                request,
                f"Product {update_form.data['name']} has been updated"
                f" in the system")
            return redirect(reverse(index))
        else:
            return render(request, 'products/update_product.template.html', {
                      'form': update_form
                      })
    else:
        update_form = ProductForm(instance=product_to_update)
        return render(request, 'products/update_product.template.html', {
                      'form': update_form
                      })

@login_required
@permission_required('products.delete_product')
def delete_product(request, product_id):
    product_to_delete = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_to_delete.delete()
        return redirect(reverse(index))

