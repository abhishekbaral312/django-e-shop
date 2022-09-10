"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import index, login, signup,cart,store
from .views.login import logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.store import Store
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', index.Index.as_view(), name='homepage'),
    path('signup', signup.SignUp.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart',auth_middleware(cart.Cart.as_view()),name='cart'),
    path('check-out',auth_middleware(CheckOut.as_view()),name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name ='orders'),
    path('store',store.Store.as_view(),name='store')
]
