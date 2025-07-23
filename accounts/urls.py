from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('', views.IndexTZ, name='IndexTZ'),
    path('ShopTZ/', views.ShopTZ, name='ShopTZ'),
    path('AboutTZ/', views.AboutTZ, name='AboutTZ'),
    path('ProDetailTZ/', views.ProDetailTZ, name='ProDetailTZ'),
    path('BlogTZ/', views.BlogTZ, name='BlogTZ'),
    path('BlogDetailTZ/', views.BlogDetailTZ, name='BlogDetailTZ'),
    path('LoginTZ/', views.LoginTZ, name='LoginTZ'),
    path('CartTZ/', views.CartTZ, name='CartTZ'),
    path('ConfirmTZ/', views.ConfirmTZ, name='ConfirmTZ'),
    path('CheckoutTZ/', views.CheckoutTZ, name='CheckoutTZ'),
    path('ContactTZ/', views.ContactTZ, name='ContactTZ'),


]