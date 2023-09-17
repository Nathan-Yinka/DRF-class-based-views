from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=99.99, max_digits=5, decimal_places=2)
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def __str__(self):
        return self.title
    
    def get_discount(self):
        return "123"
    