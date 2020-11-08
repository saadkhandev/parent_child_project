from django.urls import path, include
from rest_framework import routers
from app import views

app_name = "app"
router = routers.DefaultRouter()
router.register('parents', views.ParentViewSet)
router.register('children', views.ChildViewSet)

urlpatterns = [
    path('', include(router.urls))
]