from django.db import models
from django.contrib.auth.models import User


class ProductType(models.Model):
    name = models.CharField(max_length=200)


class Brand(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    image = models.ImageField(upload_to="brand_logos", blank=True)


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    image = models.ImageField(upload_to="vendor_logos", blank=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images", blank=True)


class Quote(models.Model):
    product = models.ForeignKey(
        Product, related_name="quotes", on_delete=models.CASCADE
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quote_date = models.DateTimeField()
    fuzzy_price = models.DecimalField(max_digits=9, decimal_places=2)
    fuzzy_quote_date = models.DateTimeField()
    user = models.ForeignKey("UserProfile", null=True, on_delete=models.SET_NULL)


class UserProfile(models.Model):
    USER_STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
        ("SUSPENDED", "Suspended"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=0)
    status = models.CharField(
        max_length=10, choices=USER_STATUS_CHOICES, default="ACTIVE"
    )


class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_start = models.DateTimeField()
    session_end = models.DateTimeField()
