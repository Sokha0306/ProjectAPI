from django.db.models import Count
from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets

from .authentication import QueryParamAccessTokenAuthentication
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, DecimalField, ExpressionWrapper



# Create your views here.

from django.shortcuts import redirect


def protected_api(request):
    token = request.GET.get('token')
    if not token:
        return JsonResponse({'error': 'Token is required'}, status=400)

    if not AccessToken.objects.filter(token=token, is_active=True).exists():
        return JsonResponse({'error': 'Invalid or inactive token'}, status=403)
    
    # Query all items
    items = Item.objects.all().values('id', 'name', 'description', 'price')
    return JsonResponse({'items': ProductList(items)})




from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Sum, F, ExpressionWrapper, DecimalField
from django.http import Http404
from django.contrib.contenttypes.models import ContentType
from .models import (
    TopBanner, Menu, SubMenu, Slide, Gallery, NewArrivals, PopularItems,
    Footer, FooterLink, AboutUs, Privacy, ProductList, CartItem, Blog, BlogDetails
)

# Helper: Common context for all views
def get_common_context():
    links = list(FooterLink.objects.all())
    about_links = links[:3]
    customer_links = links[3:6]

    return {
        'Menus': Menu.objects.annotate(sub_count=Count('submenus')),
        'SubMenus': SubMenu.objects.all(),
        'topBanner': TopBanner.objects.first(),
        'sliders': Slide.objects.all(),
        'footers': Footer.objects.all(),
        'links': links,
        'about_links': about_links,
        'customer_links': customer_links,
    }


def IndexTZ(request):
    context = get_common_context()
    context.update({
        'new_arrivals': NewArrivals.objects.all(),
        'popular_items': PopularItems.objects.all(),
        'gallerys': Gallery.objects.all(),
    })
    return render(request, 'TZ/index.html', context)


def ShopTZ(request):
    context = get_common_context()
    context.update({
        'lip_gloss': ProductList.objects.filter(ProCategoryID__CategoryName__iexact='Lip Gloss'),
        'blush': ProductList.objects.filter(ProCategoryID__CategoryName__iexact='Blush'),
        'lip_liner_gloss_set': ProductList.objects.filter(ProCategoryID__CategoryName__iexact='Lip Liner & Gloss Set'),
    })
    return render(request, 'TZ/shop.html', context)





def AboutTZ(request):
    context = get_common_context()
    context.update({
        'abtus': AboutUs.objects.all(),
    })
    return render(request, 'TZ/about.html', context)


def PrivacyTZ(request):
    context = get_common_context()
    context.update({
        'privacys': Privacy.objects.all(),
    })
    return render(request, 'TZ/PrivacyPolicy.html', context)


def ProDetailTZ(request, type, id):
    if type == 'new':
        product = get_object_or_404(NewArrivals, id=id)
    elif type == 'popular':
        product = get_object_or_404(PopularItems, id=id)
    elif type == 'list':
        product = get_object_or_404(ProductList, id=id)
    else:
        return render(request, '404.html')

    context = get_common_context()
    context.update({
        'prodetail': product,
        'type': type,
    })
    return render(request, 'TZ/product_details.html', context)


def BlogTZ(request):
    context = get_common_context()
    context.update({
        'blogs': Blog.objects.all(),
    })
    return render(request, 'TZ/blog.html', context)


def BlogDetailTZ(request, blog_id):
    context = get_common_context()
    try:
        blog = Blog.objects.get(id=blog_id)
        blog_detail = blog.detail
    except Blog.DoesNotExist:
        blog = None
        blog_detail = None
    except BlogDetails.DoesNotExist:
        blog_detail = None

    context.update({
        'blog': blog,
        'blogdetail': blog_detail,
    })
    return render(request, 'TZ/blog-details.html', context)


def LoginTZ(request):
    return render(request, 'TZ/login.html', get_common_context())


def CartTZ(request):
    context = get_common_context()
    cart = CartItem.objects.filter(user=request.user)

    total_price = sum(item.price * item.quantity for item in cart)

    context.update({
        'cart': cart,
        'total_price': total_price,
    })
    return render(request, 'TZ/cart.html', context)



def ConfirmTZ(request):
    return render(request, 'TZ/confirmation.html', get_common_context())


def CheckoutTZ(request):
    return render(request, 'TZ/checkout.html', get_common_context())


def ContactTZ(request):
    return render(request, 'TZ/contact.html', get_common_context())


def ConfirmationTZ(request):
    return render(request, 'TZ/confirmation.html', get_common_context())


from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

def add_to_cart(request, product_type, product_id):
    if not request.user.is_authenticated:
        return redirect('LoginTZ')

    model_map = {
        'list': ProductList,
        'popular': PopularItems,
        'new': NewArrivals,
    }

    model = model_map.get(product_type)
    if not model:
        return redirect('ShopTZ')

    product = get_object_or_404(model, id=product_id)
    content_type = ContentType.objects.get_for_model(model)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=product_id,
        defaults={
            'quantity': 1,
            'price': product.get_price,
        }
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('CartTZ')







def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.subtotal for item in cart_items)

    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()

    context = {
        'sliders': sliders,
        'Menus': Menus,
        'SubMenus': SubMenus,
        'topBanner': topBanner,
        'footers': footers,
        'links': links,
        'cart': cart_items,
        'total_price': total_price,
    }
    return render(request, 'TZ/cart.html', context)





def remove_from_cart(request, product_type, product_id):
    if not request.user.is_authenticated:
        return redirect('LoginTZ')

    if request.method != "POST":
        # optionally redirect or raise error
        return redirect('CartTZ')

    model_map = {
        'list': ProductList,
        'popular': PopularItems,
        'new': NewArrivals,
    }
    
    model = model_map.get(product_type)
    if not model:
        return redirect('CartTZ')

    content_type = ContentType.objects.get_for_model(model)

    cart_item = CartItem.objects.filter(
        user=request.user,
        content_type=content_type,
        object_id=product_id,
    ).first()

    if cart_item:
        cart_item.delete()

    return redirect('CartTZ')






def product_list(request):
    products = ProductList.objects.all()
    popular_items = PopularItems.objects.all()
    new_arrivals = NewArrivals.objects.all()

    context = {
        'products': products,
        'popular_items': popular_items,
        'new_arrivals': new_arrivals,
    }
    return render(request, 'TZ/product_list_in_cart.html', context)



class ProductListViewSet(viewsets.ModelViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # requires token

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset
   


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # requires token

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset
    


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # requires token

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset
    

class BlogDetailViewSet(viewsets.ModelViewSet):
    queryset = BlogDetails.objects.all()
    serializer_class = BlogDetailSerializer
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # requires token

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset
    


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # requires token

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset



class QRCodeViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # requires token

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # requires token

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset
    

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer  # create this serializer if not created
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset