from django.urls import path, include
from .views import Companyviewset, Employeeviewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies', Companyviewset)
router.register(r'employees', Employeeviewset)

urlpatterns = [
    path('', include(router.urls)),
]