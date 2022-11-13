from rest_framework import serializers

from .models import *


class EmployeeModelSerializer(serializers.ModelSerializer):
    """Employees serializer"""
    class Meta:
        model = EmployeeAdminModel
        exclude = ('id', 'employee_block')


class GalleryImageModelSerializer(serializers.ModelSerializer):
    """Gallery images serializer"""
    class Meta:
        model = GalleryImageModel
        exclude = ('id', 'gallery_block')


class ProductModelSerializer(serializers.ModelSerializer):
    """Products serializer"""
    class Meta:
        model = ProductModel
        exclude = ('id', 'products_block')


class FormBlockSerializer(serializers.ModelSerializer):
    """Form serializer"""
    class Meta:
        model = FormBlockAdminModel
        exclude = ('id',)


class LandingModelAdminSerializer(serializers.ModelSerializer):
    """Landing context serializer"""
    products = ProductModelSerializer(many=True, read_only=True)
    images = GalleryImageModelSerializer(many=True, read_only=True)
    employees = EmployeeModelSerializer(many=True, read_only=True)

    class Meta:
        model = LandingModel
        exclude = ('id',)
