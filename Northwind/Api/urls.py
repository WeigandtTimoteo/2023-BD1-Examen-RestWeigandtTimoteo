from django.contrib import admin
from django.urls import path, include
from Api import views

urlpatterns = [
    #Customers
    path('customers/', views.customers),
    path('customers/<str:customerid>/', views.customer),

    #Suppliers
    path('suppliers/', views.suppliers),
    path('suppliers/<int:supplierid>/', views.supplier),

    #Categories
    path('categories/', views.categories),
    path('categories/<int:categoryid>/', views.category),

    #Products
    path('products/', views.products),
    path('products/<int:productid>/', views.product),

    #Orders
    path('orders/', views.orders),
    path('orders/<int:orderid>/', views.order),

    #OrderDetails
    path('orderDetails/', views.orderdetails),
    path('orderDetails/<int:orderid>/', views.orderdetail),

    #Employees
    path('employees/', views.employees),
    path('employees/<int:employeeid>/', views.employee),

    #Ejemplos y Pruebas
    path('prueba/MayorAFecha/', views.MayorAFecha),
    path('prueba/MenorAFecha/', views.MenorAFecha),
    path('prueba/EntreFechas/', views.EntreFechas),
    path('prueba/StartsWith/', views.StartsWith),
    path('prueba/EndsWith/', views.EndsWith),
    path('prueba/OrderBy/', views.OrderBy),
    path('prueba/OrderByReverse/', views.OrderByReverse),

    #Path del examen
    path('examen/punto1', views.punto1)
]