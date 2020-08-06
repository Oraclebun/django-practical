from django.urls import path
import products.views

urlpatterns = [
    path('', products.views.index),
    path('create', products.views.input_product,
         name="create_product_route"),
    path('update/<product_id>', products.views.update_product,
         name="update_product_route"),
    path('delete/<product_id>', products.views.delete_product,
         name="delete_product_route")
]
