from rest_framework import serializers
from .models import User, Villager, Driver, Leader, Seller

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'role']

class VillagerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Villager
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        villager = Villager.objects.create(user=user, **validated_data)
        return villager

class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Driver
        fields = ['user', 'license_number']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        driver = Driver.objects.create(user=user, **validated_data)
        return driver

class LeaderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Leader
        fields = ['user', 'position']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        leader = Leader.objects.create(user=user, **validated_data)
        return leader

class SellerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Seller
        fields = ['user', 'shop_name']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        seller = Seller.objects.create(user=user, **validated_data)
        return seller
