from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
def home(request, c_slug=None):
    c_page = None
    obj1 = None
    if c_slug!= None:
        c_page = get_object_or_404(catg, slug=c_slug)
        obj1 = prod.objects.filter(category=c_page, available=True)

    else:

        obj1 = prod.objects.all().filter(available=True)
    cat = catg.objects.all()
    paginator=Paginator(obj1,3)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)


    return render(request, 'index.html', {'obj': obj1, 'ct': cat,'pg':pro})

def prodDetails(request,c_slug,product_slug):
    try:
        pro=prod.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render(request,'item.html',{'pr':pro})
def search(request):
    pro=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        pro=prod.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':pro})
