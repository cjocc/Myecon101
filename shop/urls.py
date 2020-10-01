from django.contrib import admin
from django.urls import path

from shop import views

urlpatterns = [
    path("", views.index, name="Shop Home"),
    path('about/', views.about, name="About us"),
    path('contact/', views.contact, name="Contact us "),
    path('tracking/', views.tracking, name="TrackStatus"),
    path('product', views.product, name="Product"),
    path('checkout', views.checkout, name="Checkout"),
    path('search', views.search, name="Search"),
]
