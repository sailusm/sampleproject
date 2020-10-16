"""onlinemobileshop URL Configuration

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
from django.urls import path

from product.views import createBrand,editBrand,deleteBrand,createMobile,mobileView,orders,viewOrder,orderUpdate,trackOrders,searchBrand,register,loginPage,homePage,test,logOut,viewUserOrder
from product.views import cancelOrder,adminPage
urlpatterns = [
    path('create/', createBrand,name='createbrand'),
    path('edit/<int:pk>',editBrand,name='editbrand'),
    path('delete/<int:pk>', deleteBrand, name='deletebrand'),
    path('product/',createMobile, name='product'),
    path('buy/<int:pk>', mobileView, name='buy'),
    path('order/<int:pk>',orders,name='order'),
    path('vieworder/',viewOrder, name='vieworder'),
    path('orderupdate/<int:pk>', orderUpdate, name='orderupdate'),
    path('track/', trackOrders),
    path('search/',searchBrand),
    path('register/',register,name='register'),
    path('login/', loginPage,name="login"),
    path("home/", homePage, name="homepage"),
    path("test/", test, name="test"),
    path("adminpage/", adminPage, name="adminpage"),
    path("logout/", logOut, name="logout"),
    path("userorder/", viewUserOrder, name="viewuserorder"),
path("cancel/<int:pk>", cancelOrder, name="cancel"),


]
