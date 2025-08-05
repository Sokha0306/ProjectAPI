from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('Product_List', ProductListViewSet)
router.register('Product_Detail', ProductDetailViewSet)
router.register('blog', BlogViewSet)
router.register('blog_Detail', BlogDetailViewSet)
router.register('product_Category', CategoryViewSet)
router.register('qr_codes', QRCodeViewSet)
router.register('orders', OrderViewSet)
router.register('Add_tocart', CartItemViewSet)



urlpatterns = [

    path('API/', include(router.urls)),

    path('data/', protected_api),

    path('', views.IndexTZ, name='IndexTZ'),

    path('ShopTZ/', ShopTZ, name='ShopTZ'),

    path('AboutTZ/', views.AboutTZ, name='AboutTZ'),
    
    path('product/<str:type>/<int:id>/', views.ProDetailTZ, name='ProDetailTZ'),

    path('BlogTZ/', views.BlogTZ, name='BlogTZ'),

    path('BlogDetailTZ/<int:blog_id>/', views.BlogDetailTZ, name='BlogDetailTZ'),

    path('LoginTZ/', views.LoginTZ, name='LoginTZ'),

    path('CartTZ/', views.CartTZ, name='CartTZ'),

    path('ConfirmTZ/', views.ConfirmTZ, name='ConfirmTZ'),

    path('CheckoutTZ/', views.CheckoutTZ, name='CheckoutTZ'),

    path('ContactTZ/', views.ContactTZ, name='ContactTZ'),

    path('ConfirmationTZ/', views.ConfirmationTZ, name='ConfirmationTZ'),

    path('CartTZ/', views.view_cart, name='view_cart'),

    path('cart/add/<str:product_type>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),


    path('api/remove-from-cart/<str:product_type>/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('cart/', views.view_cart, name='view_cart'),
]

# ✅ Append static URLs properly
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
