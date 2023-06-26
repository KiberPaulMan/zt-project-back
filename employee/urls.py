from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
