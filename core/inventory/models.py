from django.db import models
# Create your models here.

product_category = (
    ("FOOD", "food"),
    ("FLOWER", "flower"),
    ("LIQUID", "liquid"),
    ("VEHICLE", "vehicle"),
    ("ELECTRONIC", "electronic"),
    ("OTHERS", "other")
)


class Product(models.Model):
    web_id = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=product_category, default="OTHERS")
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ('view_item', 'View Item')
        ]

    def __str__(self):
        return self.name

