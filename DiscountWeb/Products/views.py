from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Product

def index(request):
    latest_item_list = Product.objects.order_by('-PubTime')[:5]
    #output = ','.join([q.ProductName for q in latest_item_list])
    template = loader.get_template('Products/index.html')
    context ={
        'latest_item_list':latest_item_list
    }
    return render(request,'Products/index.html',context)

def detail(request,Product_ID):
    product = get_object_or_404(Product,pk=Product_ID)
    return render(request,'Products/detail.html',{'Product':product})