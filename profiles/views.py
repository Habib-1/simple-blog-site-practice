from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def profile(request):
    if request.method=="POST" :
        profileCreate=forms.profileForm(request.POST)
        if profileCreate.is_valid():
            profileCreate.save()
            return redirect('home')
    else:
        profileCreate=forms.profileForm()
    return render(request,'sign_up.html',{'form': profileCreate})