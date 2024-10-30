from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def addCategory(request):
    if request.method=="POST" :
        category=forms.category_form(request.POST)
        if category.is_valid():
            category.save()
            return redirect('home')
    else:
        category=forms.category_form()
    return render(request,'post.html',{'form':category})