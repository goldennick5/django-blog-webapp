from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def homepage(request):
    return render(request, 'homepage.html')

def posts(request):
    all_posts = Post.objects.all()

    posts_per_page = 3  

    paginator = Paginator(all_posts, posts_per_page)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }

    return render(request, 'posts.html', context)




