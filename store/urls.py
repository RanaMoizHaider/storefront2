from django.urls import path
from . import views
from rest_framework.decorators import api_view

# URLConf
urlpatterns = [
    path('products/', views.product_list)
]
