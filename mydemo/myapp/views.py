from django.shortcuts import render,redirect
from django. http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from.forms import OrderForm,CreateUserForm
from .models import *


def registerpage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form =CreateUserForm(request.POST)
        if form .is_valid():
            form.save()
        context={'form':form}
          
        return render(request,'accounts/register.html',context)
    
def loginpage(request):
    
    context={}
          
    return render(request,'accounts/login.html',context)

def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter( status='delivered').count()
    pending=orders.filter( status='pending').count()
    
  
    
    context={'orders':orders,'customers':customers,'total_orders':total_orders
             ,'pending':pending,'delivered':delivered}
    
    return render(request,'accounts/dashboard.html', context)

def products(request):
    products=Product.objects.all()
    return render(request,'accounts/products.html',{"products":products})


def customer(request, pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders= customer.order_set.all()
    order_count=orders.count()
    
    context={'customer':customer,'orders':orders,'order_count':order_count}
    return render(request,'accounts/customer.html',context)

def createorder(request):
    form=OrderForm()
    if request.method=='POST':
       # print('printing POST',request.POST)
       form=OrderForm(request.POST)
    if form.is_valid():
           form.save()
           return redirect('/')
    context={'form':form}
    
    return render(request,'accounts/order_form.html', context)

def updateorder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
       # print('printing POST',request.POST)
       form=OrderForm(request.POST,instance=order)
    if form.is_valid():
           form.save()
           return redirect('/')
    context={'form':form}
    
    return render(request,'accounts/order_form.html', context)

def deleteorder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
      order.delete()
      return redirect('/')

    context={'item':order}
    
    return render(request,'accounts/delete.html', context)
  

