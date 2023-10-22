from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    New_arrival = 'New Arrival'
    Computer_Accessires = 'Computer Accessires'
    Watches = 'Watch'
    Mobiles = 'Mobile'
    Laptops = 'Laoptop'
    categories = [(New_arrival, 'New-Arrival'), (Computer_Accessires, 'Computer Accessires'), (Watches, 'Watch'),
                  (Mobiles, 'Mobile'), (Laptops, 'Laptop')]
    category = models.CharField(max_length=20, choices=categories, default=New_arrival)
    Subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    desc = models.CharField(max_length=300)
    list_Date = models.DateField()

    def __str__(self):
        return self.product_name
