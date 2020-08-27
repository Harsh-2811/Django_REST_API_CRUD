from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Email = validated_data.get('Email', instance.Email)
        instance.Mobile_No = validated_data.get('Mobile_No', instance.Mobile_No)
        instance.Department = validated_data.get('Department', instance.Department)

        instance.save()
        return instance