from django.db import models


from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)

    class Meta:

        verbose_name_plural = 'categories'

    # Category Shirt, Shoes..
    def __str__(self):

        return self.name


    def get_absolute_url(self):

        return reverse('list-category', args=[self.slug])



class Product(models.Model):

    #FK 

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)


    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    image = models.ImageField(upload_to='images/')


    class Meta:

        verbose_name_plural = 'products'


    #product(1)-->title
    
    def __str__(self):

        return self.title



    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])

class UserBrowsingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联到用户
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # 关联到商品
    browsing_time = models.DateTimeField(auto_now_add=True)  # 自动记录浏览时间

    class Meta:
        verbose_name_plural = ' Browsing Histories'
        ordering = ['-browsing_time']  # 默认按时间倒序排列

    def __str__(self):
        return f"{self.user.username} viewed {self.product.title}"