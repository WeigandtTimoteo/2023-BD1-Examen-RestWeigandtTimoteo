from django.shortcuts import render
from rest_framework import response, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Api.serializers import *
from Api.models import *

# Create your views here.

# CRUD Customers
@api_view(['GET', 'POST'])
def customers(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customer(request, customerid):
    try:
        customer = Customers.objects.get(customerid=customerid)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomersSerializer(customer, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomersSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD Suppliers
@api_view(['GET', 'POST'])
def suppliers(request):
    if request.method == 'GET':
        suppliers = Suppliers.objects.all()
        serializer = SuppliersSerializer(suppliers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuppliersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def supplier(request, supplierid):
    try:
        supplier = Suppliers.objects.get(supplierid=supplierid)
    except Suppliers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SuppliersSerializer(supplier, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuppliersSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD Categories
@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category(request, categoryid):
    try:
        category = Categories.objects.get(categoryid=categoryid)
    except Categories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriesSerializer(category, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriesSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD Products
@api_view(['GET', 'POST'])
def products (request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product (request, productid):
    try:
        proyecto = Products.objects.get(productid=productid)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(product, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD Orders
@api_view(['GET', 'POST'])
def orders(request):
    if request.method == 'GET':
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def order(request, orderid):
    try:
        order = Orders.objects.get(orderid=orderid)
    except Orders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrdersSerializer(order, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrdersSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD Orderdetails
@api_view(['GET', 'POST'])
def orderdetails(request):
    if request.method == 'GET':
        orderdetails = OrderDetails.objects.all()
        serializer = OrderDetailsSerializer(orderdetails, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def orderdetail(request, orderid):
    try:
        orderdetail = OrderDetails.objects.get(orderid=orderid)
    except OrderDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderDetailsSerializer(orderdetail, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderDetailsSerializer(orderdetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        orderdetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD Employees
@api_view(['GET', 'POST'])
def employees(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employee(request, employeeid):
    try:
        employee = Employees.objects.get(employeeid=employeeid)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeesSerializer(employee, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeesSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#----------------------------------------------------
# Pruebas y Ejemplos
#----------------------------------------------------

@api_view(['GET'])
def FechaMayor(request):
    orders = Orders.objects.filter(orderdate__gt="1996-12-24")
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def FechaMenor(request):
    orders = Orders.objects.filter(orderdate__lt="1996-12-24")
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def FechaRango(request):
    orders = Orders.objects.filter(orderdate__range=("1996-12-24","1997-1-1"))
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def EmpiezaCon(request):
    customers = Customers.objects.filter(contactname__startswith="A")
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TerminaCon(request):
    customers = Customers.objects.filter(contactname__endswith="a")
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Ordenado(request):
    customers = Customers.objects.all().order_by('contactname')
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def OrdenadoAlReves(request):
    customers = Customers.objects.all().order_by('-contactname')
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)