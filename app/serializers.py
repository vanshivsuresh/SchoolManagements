# projects/serializers.py

from rest_framework import serializers
from .models import SchoolManagements

class SchoolManagementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolManagements
        fields = '__all__'
