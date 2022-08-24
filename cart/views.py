from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from home.models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def cart_details(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlists.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.pdt.price*i.quts)
            count+=i.quts
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prodt=prod.objects.get(id=product_id)
    try:
        ct=cartlists.objects.get(cart_id=c_id(request))
    except cartlists.DoesNotExist:
        ct=cartlists.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(pdt=prodt,cart=ct)
        if c_items.quts < c_items.pdt.stock:
            c_items.quts+=1
            c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(pdt=prodt,quts=1,cart=ct)
        c_items.save()
    return redirect('cartDetails')



def min_cart(request,product_id):

    ct=cartlists.objects.get(cart_id=c_id(request))
    pro=get_object_or_404(prod,id=product_id)
    c_items=items.objects.get(pdt=pro,cart=ct)
    if c_items.quts>1:
        c_items.quts-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')



def cart_delete(request,product_id):
    ct=cartlists.objects.get(cart_id=c_id(request))
    pro=get_object_or_404(prod,id=product_id)
    c_items=items.objects.get(pdt=pro,cart=ct)
    c_items.delete()
    return redirect('cartDetails')

