from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.views import *


# @swagger_auto_schema(
#     method='get',
#     responses={200: OrderSerializers(many=True)}
# )
# @swagger_auto_schema(
#     method='post',
#     request_body=OrderSerializers(),
#     responses={201: OrderSerializers()}
# )
# @api_view(['GET', 'POST'])

# def order_get_post(request):
#     if request.method == 'GET':
#         actors = Order.objects.all()
#         serializer = OrderSerializers(actors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'POST':
#         serializer = OrderSerializers(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#          serializer.save()
#          return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderApi(APIView):
    @swagger_auto_schema(request_body=OrderSerializers)
    def post(self, request):
        serializer = OrderSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializers(order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class OrderDetailApi(APIView):
    def get(self, request, slug):
        # order = get_object_or_404(Order , pk = pk)
        order = Order.objects.get(slug=slug)
        serializer = OrderSerializers(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        # order = get_object_or_404(Order , slug = slug)
        order = Order.objects.get(slug=slug)
        serializer = OrderSerializers(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class EmployeesApi(APIView):
    @swagger_auto_schema(request_body=EmployeesSerializers)
    def post(self, request):
        serializer = EmployeesSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializers(employees, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EmployeesDetailApi(APIView):
    def get(self, request, slug):
        employees = Employees.objects.get(slug=slug)
        serializer = EmployeesSerializers(employees)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        employees = Employees.objects.get(slug=slug)
        serializer = EmployeesSerializers(employees, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CustomerApi(APIView):
    @swagger_auto_schema(request_body=CustomerSerializers)
    def post(self, request):
        serializer = CustomerSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializers(customer, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CustomerDetailApi(APIView):
    def get(self, request, slug):
        customer = Customer.objects.get(slug=slug)
        serializer = CustomerSerializers(customer)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        customer = Customer.objects.get(slug=slug)
        serializer = CustomerSerializers(customer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

