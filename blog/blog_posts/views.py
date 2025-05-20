from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def blog_home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_posts/blog_home.html', {'posts': posts})

def single_post_page(request, post_id):
    single_post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_posts/single_post.html', {'single_post': single_post})

@login_required(login_url='/users/login/')
def new_post(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('blog_home')  # Corrected line
    else: 
        form = forms.CreatePost()
    return render(request, 'blog_posts/new_post.html', {'form': form})
