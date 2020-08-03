from django.shortcuts import render, HttpResponse, redirect, reverse
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
        if input_form.is_valid(): #3
            input_form.save() #4
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
