from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def home_view(request : HttpRequest):

    posts = Post.objects.all()
    return render(request, "main/home.html", {"posts" : posts})

def create_post_view(request : HttpRequest):

    if request.method == "POST":
        new_post = Post(title = request.POST["title"], 
                        content = request.POST["content"], 
                        is_published = request.POST.get("is_published") == "on", 
                        published_at = request.POST["published_at"],
                        cover = request.FILES["cover"])
        new_post.save()
        return redirect('main:home_view')

    return render(request, "main/create.html")

def post_details_view(request : HttpRequest, post_id:int):
    post = Post.objects.get(pk = post_id)
    return render(request, "main/post_details.html", {"post" : post})


def update_post_view(request : HttpRequest, post_id:int):
    post = Post.objects.get(pk = post_id)
    
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.is_published = request.POST.get("is_published") == "on"
        if "cover" in request.FILES: post.cover = request.FILES["cover"]
        post.save()
        
        return redirect("main:post_details_view", post_id = post.id)
    
    return render(request, "main/post_update.html", {"post" : post})

def delete_post_view(request : HttpRequest, post_id:int):
    post = Post.objects.get(pk = post_id)
    post.delete()
    return redirect('main:home_view')