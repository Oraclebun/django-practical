from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Product, ProductInstance
from .forms import ProductForm, ProductInstanceFormSet, SearchForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

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
            instance_formset = ProductInstanceFormSet(
                request.POST, instance=new_product)
            if instance_formset.is_valid():
                new_product.save()
                instance_formset.save()
                messages.success(request,
                                 f"New Product {input_form.data['name']}"
                                 f"has been entered into the system")
            return redirect(reverse(index))
        else:
            return render(request, 'products/input_product.template.html', {
                          'form': input_form,
                          'formset': instance_formset
                          })
    else:
        input_form = ProductForm()
        instance_formset = ProductInstanceFormSet()
        return render(request, 'products/input_product.template.html', {
            'form': input_form,
            'formset': instance_formset
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
            update_formset = ProductInstanceFormSet(
                request.POST, instance=product_to_update)
            if update_formset.is_valid():
                editted_product.save()
                update_formset.save()
            messages.success(
                request,
                f"Product {update_form.data['name']} has been updated"
                f" in the system")
            return redirect(reverse(index))
    else:
        update_form = ProductForm(instance=product_to_update)
        update_formset = ProductInstanceFormSet(instance=product_to_update)
        return render(request, 'products/update_product.template.html', {
                      'form': update_form,
                      'formset': update_formset
                      })


@login_required
@permission_required('products.delete_product')
def delete_product(request, product_id):
    product_to_delete = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_to_delete.delete()
        messages.success(
                request,
                f"Product {product_to_delete.name} has been deleted")
        return redirect(reverse(index))


@login_required
@permission_required('products.input_product_instance')
def input_product_instance(request):
    if request.method == 'POST':
        input_form = ProductInstanceForm(request.POST)

        # if the form is validated
        if input_form.is_valid():
            input_form.save()
            product = get_object_or_404(Product, pk=int(input_form.data['product']))
            messages.success(
                request,
                f"New Product Instance {product} has been"
                f" entered into the system")
            return redirect(reverse(index))
        else:
            return render(request, 'products/input_product_instance.template.html', {
                          'form': input_form
                          })
    else:
        input_form = ProductInstanceForm()
        return render(request, 'products/input_product_instance.template.html', {
            'form': input_form
        })


@login_required
@permission_required('products.update_product_instance')
def update_product_instance(request, product_instance_id):
    product_instance_to_update = get_object_or_404(
        ProductInstance, pk=product_instance_id)

    if request.method == 'POST':
        update_form = ProductInstanceForm(
            request.POST, instance=product_instance_to_update)
        if update_form.is_valid():
            update_form.save()
            messages.success(
                request,
                f"Product {update_form.data['product']} has been updated"
                f" in the system")
            return redirect(reverse(index))
    else:
        update_form = ProductInstanceForm(instance=product_instance_to_update)
        return render(request, 'products/update_product_instance.template.html', {
                      'form': update_form
                      })
