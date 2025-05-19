from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import HttpResponse

# Create your views here.
def blog_home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_posts/blog_home.html', {'posts': posts})

def single_post_page(request, post_id):
    single_post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_posts/single_post.html', {'single_post': single_post})