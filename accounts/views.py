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




def IndexTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    gallerys = Gallery.objects.all()
    new_arrivals = NewArrivals.objects.all()
    popular_items = PopularItems.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()

    context = {
        'new_arrivals': new_arrivals,
        'popular_items': popular_items,
        'sliders': sliders,
        'gallerys' : gallerys,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'footers' : footers,
        'links' : links,
    }
    return render(request, 'TZ/index.html', context)



def ShopTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    products = ProductList.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()

    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'products' : products,
        'footers' : footers,
        'links' : links,
    }
    return render(request, 'TZ/shop.html', context)
    

def AboutTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    abtus = AboutUs.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'abtus' : abtus,
        'footers' : footers,
        'links' : links,
        
    }
    return render(request, 'TZ/about.html', context)



def PrivacyTZ(request) :
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    privacys = Privacy.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'privacys' : privacys,
        'footers' : footers,
        'links' : links,
        
    }
    return render(request, 'TZ/PrivacyPolicy.html', context)



def ProDetailTZ(request, type, id):
    # Determine which model to get the product from
    if type == 'new':
        product = get_object_or_404(NewArrivals, id=id)
    elif type == 'popular':
        product = get_object_or_404(PopularItems, id=id)
    elif type == 'list':
        product = get_object_or_404(ProductList, id=id)
    else:
        return render(request, '404.html')  # or raise Http404

    context = {
        'prodetail': product,
        'type': type,
        'Menus': Menu.objects.annotate(sub_count=Count('submenus')),
        'SubMenus': SubMenu.objects.all(),
        'topBanner': TopBanner.objects.first(),
        'sliders': Slide.objects.all(),
        'footers': Footer.objects.all(),
        'links': FooterLink.objects.all(),
    }
    return render(request, 'TZ/product_details.html', context)


def BlogTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    blogs = Blog.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'blogs' : blogs,
        'footers' : footers,
        'links' : links,
        
    }
    return render(request, 'TZ/blog.html',context)


def BlogDetailTZ(request, blog_id):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()

    try:
        blog = Blog.objects.get(id=blog_id)
        blog_detail = blog.detail  
    except Blog.DoesNotExist:
        blog = None
        blog_detail = None
    except BlogDetails.DoesNotExist:
        blog_detail = None

    context = {
        'sliders': sliders,
        'Menus': Menus,
        'SubMenus': SubMenus,
        'topBanner': topBanner,
        'blog': blog,
        'blogdetail': blog_detail,
        'footers' : footers,
        'links' : links,
    }
    return render(request, 'TZ/blog-details.html', context)



def LoginTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'footers' : footers,
        'links' : links,
        
    }
    return render(request, 'TZ/login.html', context)

def CartTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()

    cart = CartItem.objects.filter(user=request.user)

    total_price = cart.aggregate(
        total=Sum(ExpressionWrapper(F('price') * F('quantity'), output_field=DecimalField()))
    )['total']

    context = {
        'sliders': sliders,
        'Menus': Menus,
        'SubMenus': SubMenus,
        'topBanner': topBanner,
        'footers': footers,
        'links': links,
        'cart': cart,
        'total_price': total_price,
    }

    return render(request, 'TZ/cart.html', context)


def ConfirmTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'footers' : footers,
        'links' : links,
        
    }
    return render(request, 'TZ/confirmation.html', context)

def CheckoutTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'footers' : footers,
        'links' : links,
        
    }
    return render(request, 'TZ/checkout.html', context)

def ContactTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'footers' : footers,
        'links' : links,
        
    }
    return render(request, 'TZ/contact.html', context)

def CheckoutTZ(request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'footers' : footers,
        'links' : links,
        
    }
    return render(request, 'TZ/checkout.html', context)

def ConfirmationTZ (request):
    topBanner = TopBanner.objects.first()
    Menus = Menu.objects.annotate(sub_count=Count('submenus'))
    SubMenus = SubMenu.objects.all()
    sliders = Slide.objects.all()
    footers = Footer.objects.all()
    links = FooterLink.objects.all()
    context = {
        'sliders': sliders,
        'Menus' : Menus,
        'SubMenus' : SubMenus,
        'topBanner' : topBanner,
        'footers' : footers,
        'links' : links,
        
    }
    return render(request, 'TZ/confirmation.html', context)



def add_to_cart(request, model_name, product_id):
    user = request.user
    quantity = int(request.POST.get('quantity', 1))

    try:
        content_type = ContentType.objects.get(model=model_name)
    except ContentType.DoesNotExist:
        raise Http404("Product model not found.")

    model_class = content_type.model_class()
    product = model_class.objects.get(id=product_id)

    price = product.get_price()

    cart_item, created = CartItem.objects.get_or_create(
        user=user,
        content_type=content_type,
        object_id=product_id,
        defaults={'quantity': quantity, 'price': price}
    )

    if not created:
        cart_item.quantity += quantity
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
    model_map = {
        'list': ProductList,
        'popular': PopularItems,
        'new': NewArrivals
    }

    model = model_map.get(product_type)
    if not model:
        return redirect('CartTZ')

    product = get_object_or_404(model, id=product_id)
    content_type = ContentType.objects.get_for_model(model)

    CartItem.objects.filter(user=request.user, content_type=content_type, object_id=product_id).delete()
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