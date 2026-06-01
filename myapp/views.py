from django.shortcuts import render , redirect
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User

def get_all_post(request):
    posts = Post.objects.all()
    
    return render(request,"posts.html",{
        "posts":posts
    })
    
def get_single_post(request,id):
    post = Post.objects.get(id=id)
    
    return render(request,"post.html",{
        "post":post
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        Post.objects.create(
            title = title,
            content = content
        )
        
        return redirect("get_all_post")
    
    return render(request,"create_post.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = User.objects.create_user(
            username = username,
            password = password
        )
        
        login(request, user)
        
        return redirect("get_all_post")
    
    return render(request, "register.html")

@login_required
def add_comment(request,id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        content = request.POST.get("content")
        
        Comment.objects.create(
            post=post,
            user = request.user,
            content = content
        )
        
    return redirect("get_single_post",id=id)

@login_required
def add_like(request,id):
    post = Post.objects.get(id = id)
    like , created = Like.objects.get_or_create(
        post=post,
        user = request.user
    )
    if not created:
        like.delete()
        
    return redirect("get_single_post",id=id)