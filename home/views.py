from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from blog.models import Blog
from home.forms import ContactForm, OrderForm
from home.models import Messagess
from product.models import Category, Product, Comment, Order


def home(request):
    category = Category.objects.all()
    blog = Blog.objects.all()
    product_latest = Product.objects.filter(status='True').order_by('id')
    context = {
        'category':category,
        'product_latest':product_latest,
        'blog':blog,
       }
    return render(request, 'index.html', context)

def product_single(request, id, slug,):
    product = Product.objects.get(pk=id)
    category = Category.objects.all().order_by('id')
    product_latest = Product.objects.filter(status='True').order_by('-id')
    comments = Comment.objects.all()
    context = {
        'product':product,
        'product_latest':product_latest,
        'category':category,
        'comments':comments,
    }
    return render(request, 'product_single.html', context)


def category_product(request, id, slug):
    category = Category.objects.all()
    product_latest = Product.objects.filter(status='True').order_by('-id')[:8]
    products = Product.objects.filter(category_id=id)
    paginator = Paginator(products, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'page':page,
        'category': category,
        'products': products,
        'product_latest' : product_latest,

    }
    return render(request, 'menu.html', context)


def contact_us(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Messagess()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            return redirect('home')
    form = ContactForm
    category = Category.objects.all()
    product_latest = Product.objects.filter(status='True').order_by('-id')[:8]
    context = {
        'form': form,
        'product_latest':product_latest,
        'category':category,
    }
    return render(request,'contact.html', context)


def c_product(request):
    product_latest = Product.objects.filter(status='True').order_by('-id')
    products = Product.objects.filter(category_id=id)
    paginator = Paginator(products, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'products':products,
        'page': page,
        'product_latest':product_latest,
    }
    return render(request, 'products.html', context)

def Ordeer(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.amount = form.cleaned_data['amount']
            data.category = form.cleaned_data['category']
            data.food = form.cleaned_data['food']
            data.address = form.cleaned_data['address']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            return redirect('home')
        form = OrderForm
        context = {
            'form':form,
        }
        return render(request, 'product_single.html', context)

