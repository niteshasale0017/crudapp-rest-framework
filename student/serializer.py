from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=20)
    phone = serializers.CharField(max_length=11)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.city = validate_data.get('city',instance.city)
        instance.phone = validate_data.get('phone',instance.phone)
        instance.save()
        return instance