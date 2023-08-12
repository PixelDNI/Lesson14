from django.urls import re_path, path

from .views import show_more

urlpatterns = [
    re_path(r'^product/(?P<pk>\d+)/$', show_more, name='product-detail-right'),
]