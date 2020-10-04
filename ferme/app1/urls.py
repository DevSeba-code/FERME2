from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.shop , name="home"),
    path('cart/', views.cart, name="cart"),
    path('login/',views.login_request, name = "login"),
    path('checkout/',views.checkout, name="checkout"),
    path('register/', views.registerPage, name="register"),
    # path("register/", views.register_request, name="register"),
    # path("logout/", views.logout_request, name= "logout"),
    path("contact/", views.contact, name= "contact"),
    path("about/", views.about, name= "about"),

  
]
