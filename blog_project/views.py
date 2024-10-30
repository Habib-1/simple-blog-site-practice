from django.shortcuts import render
from posts.models import Post
# Create your views here.
def home(request):
    content=Post.objects.all()
    
    return render(request,'home.html',{'data':content})