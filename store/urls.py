from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('product',views.product,name='product'),
    path('why',views.why,name='why'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('signup',views.signup,name='signup'),
    path('login',views.Loginn,name='login'),
    path('logout',views.Logoutt,name='logout'),
    path('terms&condition',views.conditions,name='terms&condition'),
    path('cart',views.cart,name='cart'),
    path('addToCart/<int:i>',views.add_to_cart,name='addToCart'),
    path('removeCartItem/<int:item_id>',views.remove_cart_item,name='removeCartItem'),
    path('increase_item/<int:item_id>',views.increase_item,name='increaseItem'),
    path('decrease_item/<int:item_id>',views.decrease_item,name='decreaseItem'),
]
