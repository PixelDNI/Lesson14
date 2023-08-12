from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category}"


class Product(models.Model):
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
        return reverse('product_detail_left', kwargs={'pk': self.id})

