from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class AccessToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.token


class TopBanner(models.Model):
    Logo= models.ImageField(upload_to='Logo/', null=True, blank=True)
    def __str__(self):
        return f'{self.id}'


class menu(models.Model):
    MenuName = models.CharField(max_length=200,null=True)
    def __str__(self):
        return f'{self.id} -> {self.MenuName}'


class SubMenu(models.Model):
    SubMenuName = models.CharField(max_length=200,null=True)
    MenuID = models.ForeignKey(menu, on_delete=models.CASCADE, null=True, related_name='submenus')
    def __str__(self):
        return f'{self.MenuID.MenuName} -> {self.SubMenuName}'


class Slide(models.Model):
    SlideName = models.CharField(max_length=200,null=True)
    SlideImage = models.ImageField(upload_to='SlideImage/', null=True, blank=True)
    SlideDescription = RichTextUploadingField(null=True)
    def __str__(self):
            return f'{self.id} -> {self.SlideName}'


class NewArrivals(models.Model):
    NewAImage = models.ImageField(upload_to='ProvideImage/', null=True, blank=True) 
    NewAName = models.CharField(max_length=200,null=True)
    NewAPrice = models.CharField(max_length=200,null=True)
    def __str__(self):
            return f'{self.id} -> {self.NewAName}  {self.NewAImage}'


class PopularItems(models.Model):
    PopIImage = models.ImageField(upload_to='ProvideImage/', null=True, blank=True)
    PopIName = models.CharField(max_length=200,null=True)
    PopIPrice = models.CharField(max_length=200,null=True)
    PopIDescription = RichTextUploadingField(null=True)
    def __str__(self):
            return f'{self.id} -> {self.PopIName}  {self.PopIImage}'


class ProductOfChoice(models.Model):
    ProCImage = models.ImageField(upload_to='ProvideImage/', null=True, blank=True)
    ProCDescription = RichTextUploadingField(null=True)
    def __str__(self):
            return f'{self.id} -> {self.ProCImage}  {self.ProCDescription}'



class ProductCategory(models.Model):
    CategoryName = models.CharField(max_length=200,null=True)
    def __str__(self):
            return f'{self.id} -> {self.CategoryName} '




class ProductList(models.Model):
    ProCategoryID = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    ProLName = models.CharField(max_length=200,null=True)
    ProLImage= models.ImageField(upload_to='ProLImage/', null=True, blank=True)
    ProLPrice= models.CharField(max_length=200,null=True)
    def __str__(self):
            return f'{self.id} -> {self.ProLName} -> {self.ProLImage} '




class ProductDetail(models.Model):
    ProListID = models.ForeignKey(ProductList, on_delete=models.CASCADE, null=True)
    ProDeName = models.CharField(max_length=200,null=True)
    ProDeDescription = RichTextUploadingField(null=True)
    ProDeQuentity= models.CharField(max_length=200,null=True)
    def __str__(self):
            return f'{self.id} -> {self.ProDeName} -> {self.ProDeDescription} '




class Blog(models.Model):
    BlogImage = models.ImageField(upload_to='BlogImage/', null=True, blank=True)
    BlogName = models.CharField(max_length=200,null=True)
    BlogDateDay = models.CharField(max_length=200,null=True)
    BlogDateMonth = models.CharField(max_length=200,null=True)
    Blogdescription = RichTextUploadingField(null=True)
    BlogRate = models.FloatField(default=0, null=True, blank=True)
    def __str__(self):
            return f'{self.id} -> {self.BlogName} -> {self.BlogImage}'
    

class BlogDetail(models.Model):
    BlogID = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    BlogDeName  = models.CharField(max_length=200,null=True)
    BlogDeImage = models.ImageField(upload_to='SlideImage/', null=True, blank=True)
    BlogDeDescription = RichTextUploadingField(null=True)
    def __str__(self):
            return f'{self.id} -> {self.BlogDeName} -> {self.BlogDeImage} '
 

class ContactUs(models.Model):
    Address = models.CharField(max_length=500,null=True)
    PhoneNum = models.CharField(max_length=200,null=True)
    Email = models.CharField(max_length=200,null=True)
    def __str__(self):
            return f'{self.id} -> {self.Address} -> {self.PhoneNum} -> {self.Email} '
 


class AboutUs(models.Model):
    Title = models.CharField(max_length=200,null=True)
    Description = RichTextUploadingField(null=True)
    def __str__(self):
            return f'{self.id} -> {self.Title} -> {self.Description}'
 

class Footer(models.Model):
    FooterName = models.CharField(max_length=200,null=True)
    def __str__(self):
            return f'{self.id} -> {self.FooterName}'
    

class QRCode(models.Model):
    qrName = models.CharField(max_length=100)
    qrImage = models.ImageField(upload_to='images/qrcodes/')
    def __str__(self): return self.qrName

    

class Order(models.Model):
    customerName = models.CharField(max_length=100)
    customerPhone = models.CharField(max_length=20)
    orderDate = models.DateTimeField(auto_now_add=True)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    QRCodeInvoice = models.ImageField(upload_to='images/QRCodeInvoice/',null=True,blank=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    productName = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField()