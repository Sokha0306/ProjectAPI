from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('proList', ProductListViewSet)
router.register('proDetail', ProductDetailViewSet)
router.register('blog', BlogViewSet)
router.register('blogDetail', BlogDetailViewSet)
router.register('proCategory', CategoryViewSet)
router.register('qrcodes', QRCodeViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
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
    path('CheckoutTZ/', views.CheckoutTZ, name='CheckoutTZ'),
    path('ConfirmationTZ/', views.ConfirmationTZ, name='ConfirmationTZ'),
]