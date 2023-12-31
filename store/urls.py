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


]
