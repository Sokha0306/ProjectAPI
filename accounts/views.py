from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework import viewsets

from .authentication import QueryParamAccessTokenAuthentication
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed


# Create your views here.

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        product = ProductList.objects.get(id=product_id)
        cart[str(product_id)] = {
            'productName': product.productName,
            'price': float(product.price),
            'quantity': 1
        }
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'TZ/cart.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')

def product_list(request):
    products = ProductList.objects.all()
    return render(request, 'TZ/shop.html', {'products': products})



def IndexTZ(request):
    new_arrivals = NewArrivals.objects.all()
    return render(request, 'TZ/index.html', {'new_arrivals': new_arrivals})


def ShopTZ(request):
    return render(request, 'TZ/shop.html')

def AboutTZ(request):
    return render(request, 'TZ/about.html')

def ProDetailTZ(request):
    return render(request, 'TZ/product_details.html')

def BlogTZ(request):
    return render(request, 'TZ/blog.html')

def BlogDetailTZ(request):
    return render(request, 'TZ/blog-details.html')

def LoginTZ(request):
    return render(request, 'TZ/login.html')

def CartTZ(request):
    return render(request, 'TZ/cart.html')

def ConfirmTZ(request):
    return render(request, 'TZ/confirmation.html')

def CheckoutTZ(request):
    return render(request, 'TZ/checkout.html')

def ContactTZ(request):
    return render(request, 'TZ/contact.html')

def CheckoutTZ(request):
    return render(request, 'TZ/checkout.html')

def ConfirmationTZ (request):
    return render(request, 'TZ/confirmation.html')

def CartTZ (request):
    return render(request, 'TZ/cart.shop.html')




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

    def get_queryset(self):
        proList_id = self.request.query_params.get('proList')
        if proList_id:
            return ProductDetail.objects.filter(ProListID=proList_id)
        return ProductDetail.objects.all()
    


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # or use custom permission
    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        return queryset
    

class BlogDetailViewSet(viewsets.ModelViewSet):
    queryset = BlogDetail.objects.all()
    serializer_class = BlogDetailSerializer

    def get_queryset(self):
        blogDetail_ID = self.request.query_params.get('blogDetail')
        if blogDetail_ID:
            return ProductDetail.objects.filter(BlogID=blogDetail_ID)
        return ProductDetail.objects.all()
    


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer



class QRCodeViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context



class ImageTypeView(viewsets.ModelViewSet):
    queryset = ImageType.objects.all()
    serializer_class = ImageTypeSerializer


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [QueryParamAccessTokenAuthentication]
    permission_classes = [AllowAny]  # or use custom permission
    def get_queryset(self):
        token = self.request.query_params.get('token')
        if not AccessToken.objects.filter(token=token, is_active=True).exists():
            from django.http import JsonResponse
            raise AuthenticationFailed("Invalid or inactive token")
        queryset = super().get_queryset()
        ProCategoryID = self.request.query_params.get('ProCategoryID')
        if ProCategoryID:
            queryset = queryset.filter(ProCategoryID=ProCategoryID)
        return queryset