from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Product, Category
from .forms import ProductForm, SearchForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.


def index(request):
    products = Product.objects.all()
    if request.GET:
        # always true query:
        queries = ~Q(pk__in=[])
        # if a name is specified, add it to the query
        if ('search_input' in request.GET and request.GET['search_input']):
            print(request.GET)
            search_input = request.GET['search_input']
            queries = queries & Q(name__icontains=search_input)\
                | Q(desc__icontains=search_input)

        # if a category is specified, add it to the query
        if 'category' in request.GET and request.GET['category']:
            print(request.GET)
            category = request.GET['category']
            queries = queries & Q(category__in=category)

        # update the existing book found
        products = products.filter(queries)
    search_form = SearchForm(request.GET)
    categories = Category.objects.all()
    cat_urls = ['view_breakfast_product', 'view_cookie_product',
                'view_grain_product', 'view_nuts_product',
                'view_baking_product', 'view_fresh_product']
    return render(request, 'products/index.template.html', {
                  'products': products,
                  'categories': categories,
                  'search_form': search_form,
                  'cat_urls': cat_urls
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


def breakfast(request):
    """View function for Breakfast Products only"""

    breakfast_products = Product.objects.filter(
        category__name__iexact='breakfast').order_by('name')
    return render(request, 'products/breakfast.template.html', {
        'breakfast_products': breakfast_products
    })


def cookies(request):
    """View function for Biscuits & Cookies only"""

    cookies_products = Product.objects.filter(
        category__name__icontains='cookie').order_by('name')
    return render(request, 'products/cookies.template.html', {
        'cookies_products': cookies_products
    })

def grains(request):
    """View function for Merle ProbeCards only"""

    breakfast_products = Product.objects.filter(
        category__name__iexact='breakfast').order_by('name')
    return render(request, 'products/breakfast.template.html', {
        'breakfast_products': breakfast_products
    })

def nuts(request):
    """View function for Merle ProbeCards only"""

    breakfast_products = Product.objects.filter(
        category__name__iexact='breakfast').order_by('name')
    return render(request, 'products/breakfast.template.html', {
        'breakfast_products': breakfast_products
    })

def baking(request):
    """View function for Merle ProbeCards only"""

    breakfast_products = Product.objects.filter(
        category__name__iexact='breakfast').order_by('name')
    return render(request, 'products/breakfast.template.html', {
        'breakfast_products': breakfast_products
    })

def fresh(request):
    """View function for Merle ProbeCards only"""

    breakfast_products = Product.objects.filter(
        category__name__iexact='breakfast').order_by('name')
    return render(request, 'products/breakfast.template.html', {
        'breakfast_products': breakfast_products
    })

def view_product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.template.html', {
        'product': product
    })
