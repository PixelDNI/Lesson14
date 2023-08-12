from django.db import models
from django.urls import reverse

from left.models import Category


# Create your models here.
class ProductRight(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    price = models.IntegerField()
    availability = models.IntegerField()
    date_of_producing = models.DateField()
    description = models.TextField()

    def show_category(self):
        category_names = ", ".join(str(category) for category in self.category.all())
        return category_names

    def __str__(self):
        return f'{self.name} - {self.show_category()} - {self.price}$'

    def get_absolute_url(self):
        return reverse('product-detail-right', args=[str(self.id)])
