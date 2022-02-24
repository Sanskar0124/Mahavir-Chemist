from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('vmsMaster', views.vmsMaster_dashboard, name="VmsMasterDashboard"),
    path('shopMaster', views.shopMaster_dashboard, name="ShopMasterDashboard"),
]