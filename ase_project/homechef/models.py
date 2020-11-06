from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django_countries.fields import CountryField

# Create your models here.

# Model for a vendor
class Vendor(models.Model):
    name = models.CharField(max_length=30)
    imageFileName = models.CharField(max_length=30,default="profilepic4.png")
    email = models.EmailField(default="homechef302020@gmail.com")
    phone = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    address = models.TextField()
    timings = models.TextField(default="09AM - 06PM")
    food_items = models.ManyToManyField('FoodItem')
    
    def __str__(self):
        return self.name

    def food_list(self):
        return self.food_items.all()

# Model for a food item
class FoodItem(models.Model):
    itemname = models.CharField(max_length=30)
    imageFileName = models.CharField(max_length=30,default="food_img2.jpg")
    ingredients=models.ManyToManyField('Ingredients')
    description = models.TextField(max_length=100)
    vendors = models.ManyToManyField(Vendor)
    rating = models.IntegerField(default=3)
    price = models.FloatField(default = 10.0)
    discount_price = models.FloatField(blank=True,null=True)
    slug = models.SlugField()
    
    def __str__(self):
        return self.itemname
    def vendor_list(self):
        return self.vendors.all()
    def ingred_lis(self):
        return self.ingredients.all()
    def get_absolute_url(self):
        return reverse("product",kwargs={
            'slug': self.slug
        })

# Model for an ingredient
class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

# Model for item in an order
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    vendorobj = models.ForeignKey(Vendor,on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.item.itemname}"

    # Calculated total item price
    def get_total_item_price(self):
        print(self.quantity * self.item.price)
        return self.quantity * self.item.price

    # Calculate total discount price
    def get_total_discount_price(self):
        print(self.quantity * self.item.discount_price)
        return self.quantity * self.item.discount_price

    # Calculates amount saved through discount
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_price()
    
    # Calculates final price
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_price()
        else:
            return self.get_total_item_price()

# Model for order
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default = False)
    
    def __str__(self):
        return self.user.username

    # Calculated order total price
    def get_order_total(self):
        total = 0
        for orderitem in self.items.all():
            total += orderitem.get_final_price()
        return total
