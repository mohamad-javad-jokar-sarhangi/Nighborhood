from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VillagerViewSet, DriverViewSet, LeaderViewSet, SellerViewSet

# ایجاد Router برای ViewSetهای ثبت‌شده
router = DefaultRouter()
router.register(r'villagers', VillagerViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'leaders', LeaderViewSet)
router.register(r'sellers', SellerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # قرار دادن Router در URL با prefix api/
]
