from rest_framework import viewsets
from .models import Villager, Driver, Leader, Seller
from .serializers import VillagerSerializer, DriverSerializer, LeaderSerializer, SellerSerializer

class VillagerViewSet(viewsets.ModelViewSet):
    queryset = Villager.objects.all()
    serializer_class = VillagerSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class LeaderViewSet(viewsets.ModelViewSet):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
