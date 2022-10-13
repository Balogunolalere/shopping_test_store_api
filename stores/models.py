from django.db import models
#import reverse
# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
        
class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tags'
        
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Products'
    
    
