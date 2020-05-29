from django.shortcuts import render
from .models import Post
# Create your views here.
def home(reqest):
    posts = Post.objects.all()


    return render(reqest, "blog/index.html", {"post":posts[0]})