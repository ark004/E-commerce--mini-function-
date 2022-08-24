from django.urls import path
from . import views

urlpatterns=[
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('min_cart/<int:product_id>/',views.min_cart,name='min_cart'),
    path('remove/<int:product_id>/',views.cart_delete,name='remove'),

]