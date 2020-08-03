from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.template.html', {
        'products': products
    })


def input_product(request):
    if request.method == 'POST':
        input_form = ProductForm(request.POST)

        # if the form is validated
        if input_form.is_valid():
            input_form.save()
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


def update_product(request, product_id):
    product_to_update = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        update_form = ProductForm(request.POST, instance=product_to_update)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse(index))
    else:
        update_form = ProductForm(instance=product_to_update)
        return render(request, 'products/update_product.template.html', {
                      'form': update_form
                      })


def delete_product(request, product_id):
    product_to_delete = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_to_delete.delete()
        return redirect(reverse(index))
    
