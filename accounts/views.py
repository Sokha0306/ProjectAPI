from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets

from .authentication import QueryParamAccessTokenAuthentication
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed


# Create your views here.

from django.shortcuts import redirect

def add_to_cart(request, product_type, product_id):
    cart = request.session.get('cart', {})
    # Your existing logic to add product here (fetch product, update cart)

    request.session['cart'] = cart
    return redirect('CartTZ')  # <-- redirect to your desired URL name here



def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'TZ/cart.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')



def protected_api(request):
    token = request.GET.get('token')
    if not token:
        return JsonResponse({'error': 'Token is required'}, status=400)

    if not AccessToken.objects.filter(token=token, is_active=True).exists():
        return JsonResponse({'error': 'Invalid or inactive token'}, status=403)
    
    # Query all items
    items = Item.objects.all().values('id', 'name', 'description', 'price')
    return JsonResponse({'items': list(items)})







def IndexTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    new_arrivals = NewArrivals.objects.all()
    popular_items = PopularItems.objects.all()

    context = {
        'new_arrivals': new_arrivals,
        'popular_items': popular_items,
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
    }
    return render(request, 'TZ/index.html', context)



def ShopTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    products = ProductList.objects.all()

    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'products' : products,
    }
    return render(request, 'TZ/shop.html', context)
    

def AboutTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    abtus = AboutUs.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'abtus' : abtus,
        
    }
    return render(request, 'TZ/about.html', context)



def ProDetailTZ(request, id):
    product = get_object_or_404(ProductDetail, id=id)
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    topBanner = TopBanner.objects.first()
    sliders = Slide.objects.all()

    context = {
        'prodetail': product,
        'Menus': Menus,
        'SubMenus': SubMenus,
        'topBanner': topBanner,
        'sliders': sliders,
    }
    return render(request, 'TZ/product_details.html', context)

def BlogTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    blogs = Blog.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'blogs' : blogs,
        
    }
    return render(request, 'TZ/blog.html',context)




def BlogDetailTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    blogdetails = BlogDetails.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'blogdetails' : blogdetails,
        
    }
    return render(request, 'TZ/blog-details.html', context)



def LoginTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        
    }
    return render(request, 'TZ/login.html', context)

def CartTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        
    }
    return render(request, 'TZ/cart.html', context)


def ConfirmTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        
    }
    return render(request, 'TZ/confirmation.html', context)

def CheckoutTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        
    }
    return render(request, 'TZ/checkout.html', context)

def ContactTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        
    }
    return render(request, 'TZ/contact.html', context)

def CheckoutTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        
    }
    return render(request, 'TZ/checkout.html', context)

def ConfirmationTZ (request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        
    }
    return render(request, 'TZ/confirmation.html', context)

def CartTZ (request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        
    }
    return render(request, 'TZ/cart.html', context)




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



class ImageTypeView(viewsets.ModelViewSet):
    queryset = ImageType.objects.all()
    serializer_class = ImageTypeSerializer
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # requires token

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # requires token

    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset