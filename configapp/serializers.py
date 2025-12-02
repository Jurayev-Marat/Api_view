from .models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['slug']


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['slug']


class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        read_only_fields = ['slug']