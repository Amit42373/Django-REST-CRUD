from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Company, Employee
from .serializers import Companyserializer, Employeeserializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class Companyviewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Companyserializer

    @action(detail=True, methods=['get'])  #DRF decorator that allows you to define custom actions for viewsets.
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emp_serializer = Employeeserializer(emps, many = True, context={'request':request})
            return Response(emp_serializer.data)
        except company.DoesNotExist:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

class Employeeviewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer