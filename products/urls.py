from django.urls import path
import products.views

urlpatterns = [
    path('', products.views.index),
    path('create', products.views.input_product,
         name="create_product_route"),
    path('update/<product_id>', products.views.update_product,
         name="update_product_route"),
    path('delete/<product_id>', products.views.delete_product,
         name="delete_product_route"),
    path('breakfast', products.views.breakfast,
         name="view_breakfast_product"),
    path('cookies', products.views.cookies,
         name="view_cookies_product"),
    path('grains', products.views.grains,
         name="view_grains_product"),
    path('nuts', products.views.nuts,
         name="view_nuts_product"),
    path('baking', products.views.baking,
         name="view_baking_product"),
    path('fresh', products.views.fresh,
         name="view_fresh_product")
    
]
