from django.shortcuts import render
from about.models import About, Chef
from product.models import Category, Product


def about(request):
    about_latest = Product.objects.filter(status='True').order_by('-id')[:8]
    categorys = Chef.objects.all()
    context = {
        'about_latest':about_latest,
        'categorys':categorys,
       }
    return render(request, 'about.html', context)


def chef(request,id):
    category = Category.objects.all
    chef = Chef.objects.all()
    chefs = Chef.objects.get(pk=id)
    context = {
        'category':category,
        'chefs':chefs,
        'chef':chef,
    }
    return render(request, 'chefbio.html', context)






