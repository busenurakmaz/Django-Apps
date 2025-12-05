from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("randevu-al/", views.randevu_al, name="randevu_al"),
    path("psikologlar/", views.psikologlar, name="psikologlar"),
]