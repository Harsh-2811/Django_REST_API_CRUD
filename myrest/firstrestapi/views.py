from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import render,HttpResponse,redirect
# Create your views here.

class EmployeeList(APIView):

    def get(self,request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request):
        emp = request.data

        # Create an article from the above data
        serializer = EmployeeSerializer(data=emp)
        emp_saved=""
        if serializer.is_valid(raise_exception=True):
            emp_saved = serializer.save()
        return Response({"success": "Employee'{}' created successfully".format(emp_saved.Name)})




class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        emp = self.get_object(pk)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        print(pk)
        emp = self.get_object(pk)
        print(emp)
        serializer = EmployeeSerializer(emp, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            emp = self.get_object(pk)
            print(emp)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emp = self.get_object(pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)