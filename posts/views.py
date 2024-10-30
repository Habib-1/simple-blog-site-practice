from django.shortcuts import render,redirect
from . import forms
from posts.models import Post
# Create your views here.
def postForm(request):
    if request.method=="POST" :
        postCreate=forms.postForm(request.POST)
        if postCreate.is_valid():
            postCreate.save()
            return redirect('home')
    else:
        postCreate=forms.postForm()
    return render(request,'post.html',{'form':postCreate})

def edit_post(request, pk):
    post=Post.objects.get(pk=pk)
    postCreate=forms.postForm(instance=post)
    if request.method=="POST" :
        postCreate=forms.postForm(request.POST,instance=post)
        if postCreate.is_valid():
            postCreate.save()
            return redirect('home')
    
    return render(request,'post.html',{'form':postCreate})

def delete_post(request, pk):
    post=Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')