from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
    elif sort == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    else:
        phone_objects = Phone.objects.order_by('name')

    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {'phone': phone[:1][0]}
    return render(request, template, context)
