from rest_framework import serializers
from .models import Company, Employee

class Companyserializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    
    class Meta:
        model = Company
        fields = "__all__"

class Employeeserializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"