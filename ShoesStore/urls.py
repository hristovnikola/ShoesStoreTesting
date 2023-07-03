"""ShoesStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from ShoesStoreApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('shoes/', shoes, name='shoes'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutUser', logoutUser, name='logoutUser'),
    path('register/', register, name='register'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart/delete/<int:id>', delete_item, name='delete_item'),
    path('cart/delete_order/<int:id>', delete_order, name='delete_order'),
    path('checkout/<int:id>', checkout, name='checkout'),
    path('order_confirmed/', order_confirmed, name="order_confirmed"),
    path('add_shoes/', add_shoes, name='add_shoes'),
    path('shoes/details/<int:id>', shoes_details, name='shoes_details'),
    path('shoes/edit/<int:id>', add_shoes, name='shoes_edit'),
    path('shoes/delete/<int:id>', delete_shoes, name='delete_shoes'),
    path('not_allowed/', not_allowed, name='not_allowed'),
    path('cart_item/increase/<int:id>', increase_quantity, name='increase_quantity'),
    path('cart_item/decrease/<int:id>', decrease_quantity, name='decrease_quantity')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
