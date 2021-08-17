from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name= "store"),
    path('cart/', views.cart, name= "cart"),
    path('checkout/', views.checkout, name= "checkout"),
    path('products/', views.products, name="products"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('blogs/', views.blogs, name="blogs"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
]
