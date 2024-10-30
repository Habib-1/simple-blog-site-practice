from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_author(request):
    if request.method=='POST' :
        author_form=forms.authorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('home')
        
    else:
         author_form=forms.authorForm()
    return render(request,'add_author.html',{'form' : author_form})
