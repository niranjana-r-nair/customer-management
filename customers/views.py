from django.shortcuts import render

# Create your views here.
from customers.models import Customer
from customers.serializers import CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CustomerList(APIView):

    def get(self,request):
        p=Customer.objects.all()
        serializer=CustomerSerializer(p,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class CustomerDetail(APIView):

    def get(self,request,id):
        p=Customer.objects.get(id=id)
        serializer=CustomerSerializer(p)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        p=Customer.objects.get(id=id)
        serializer=CustomerSerializer(p,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,id):
        p=Customer.objects.get(id=id)
        serializer=CustomerSerializer(p,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        p=Customer.objects.get(id=id)
        p.delete()
        return Response({"msg":"delete"},status=status.HTTP_204_NO_CONTENT)