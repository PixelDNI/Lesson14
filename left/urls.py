from django.urls import path

from .views import show_more

urlpatterns = [
    path('product/<int:pk>/', show_more, name='product_detail_left'),
]