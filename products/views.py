from django.shortcuts import render, redirect
from . models import Product, Category
from . forms import ProductForm



def  showproduct(request):
    category = request.GET.get('category')

    if category == None:
        products = Product.objects.order_by('-price').filter(is_published=True)

    else:
        products = Product.objects.filter(category__name=category)
  
    categories=Category.objects.all()
    

    return render(request, 'products/showproduct.html',{'products':products, 'categories':categories})

def productdetail(request, pk):
    eachproduct=Product.objects.get(id=pk)

    return render(request, 'products/productdetail.html',{'eachproduct':eachproduct})

def addproduct(request):
    if request.method == 'POST':
        form= ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    else:
        form=ProductForm()
    return render(request, 'products/addproduct.html',{'form':form})


def updateproduct(request,pk):
    product =Product.objects.get(id=pk)

    form = ProductForm(instance=product)
    if request.method == 'POST':
        form= ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    return render(request, 'products/updateproduct.html',{'form':form})
    
def deleteproduct(request, pk):
        product =Product.objects.get(id=pk)
        product.delete()
        return redirect('showproduct')

