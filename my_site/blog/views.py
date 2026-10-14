from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html") # / django automatically looks inside the APP templates folder, so we need to point to the blog folder inside and then the file.

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
    