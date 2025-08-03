from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('proList', ProductListViewSet)
router.register('proDetail', ProductDetailViewSet)
router.register('blog', BlogViewSet)
router.register('blogDetail', BlogDetailViewSet)
router.register('proCategory', CategoryViewSet)
router.register('qrcodes', QRCodeViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('API/', include(router.urls)),

    path('', views.IndexTZ, name='IndexTZ'),

    path('ShopTZ/', ShopTZ, name='ShopTZ'),

    path('AboutTZ/', views.AboutTZ, name='AboutTZ'),

    # urls.py

    path('ProDetailTZ/<int:id>/', views.ProDetailTZ, name='ProDetailTZ'),

    path('BlogTZ/', views.BlogTZ, name='BlogTZ'),

    path('BlogDetailTZ/', views.BlogDetailTZ, name='BlogDetailTZ'),

    path('LoginTZ/', views.LoginTZ, name='LoginTZ'),

    path('CartTZ/', views.CartTZ, name='CartTZ'),

    path('ConfirmTZ/', views.ConfirmTZ, name='ConfirmTZ'),

    path('CheckoutTZ/', views.CheckoutTZ, name='CheckoutTZ'),

    path('ContactTZ/', views.ContactTZ, name='ContactTZ'),

    path('ConfirmationTZ/', views.ConfirmationTZ, name='ConfirmationTZ'),

    path('CartTZ/', views.CartTZ, name='CartTZ'),

    path('add-to-cart/<str:product_type>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
    path('cart/', views.view_cart, name='view_cart'),

    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]

# ✅ Append static URLs properly
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
