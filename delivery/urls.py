from django.urls import path, include
from rest_framework.routers import DefaultRouter
from delivery import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'deliveries', views.AddDelivery, basename="deliveries")
router.register(r'clients', views.ClientDelivery, basename="clients")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]