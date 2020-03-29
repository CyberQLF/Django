from django.shortcuts import render, render_to_response
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def main(request):
    return render(request, 'main.html')
def blog_detail(request, num):
    blog = Blog.objects.all().get(pk=num)
    return render_to_response('blog_detail.html', {'blog': blog})
def blog(request):
    paginator = Paginator(Blog.objects.all(), 10)
    page = paginator.get_page(request.GET.get('page', 1))
    return render_to_response('blog.html', {'page':page, 'blog_types':BlogType.objects.all(), 'pages':paginator})
def blog_type(request, num):
    blogs = Blog.objects.all().filter(pk=num)
    return render_to_response('blog_type.html', {'blogs':blogs})
