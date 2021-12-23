from pyexpat.errors import messages

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.models import Blog, Comment_blog
from blog.forms import Comment_detail_Form
from product.models import Comment, Category, Product


def blog(request):
    blog_latest = Blog.objects.filter(status='True').order_by('-id')
    paginator = Paginator(blog_latest, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        blog_latest = paginator.page(page)
    except PageNotAnInteger:
        blog_latest = paginator.page(1)
    except EmptyPage:
        blog_latest = paginator.page(paginator.num_pages)
    context = {
        'blog_latest':blog_latest,

        'page': page,
        }
    return render(request, 'blog.html', context)





def blog_detail(request, id):
    category = Category.objects.all()
    blog_detail = Blog.objects.get(pk=id)
    comments = Comment_blog.objects.filter(blog_id=id)
    context = {
        'category':category,
        'blog_detail':blog_detail,
        'comments':comments,
    }
    return render(request, 'blog_details.html', context)




def comment_blog(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comment_detail_Form(request.POST)
        if form.is_valid():
            data = Comment_blog()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = id
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)




