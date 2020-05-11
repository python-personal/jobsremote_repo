from django.shortcuts import render
from completeapp.models import Student
from . import forms

# Create your views her

def studview(request):
    form=forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Validation successfull')
            print('Name:',form.cleaned_data['name'])
            print('Rollno:',form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('feedback:',form.cleaned_data['feedback'])
            print('feedback:',form.cleaned_data['bot_handler'])

    return render(request,'completeapp/index.html',{'form':form})

def signup_view(request):
    form=forms.SignupForm()
    if request.method=='POST':
        form=forms.SignupForm(request.POST)
        if form.is_valid():
            print('Validation successful!!')
            print('Name:',form.cleaned_data['name'])
            print('Name:',form.cleaned_data['password'])
            print('Name:',form.cleaned_data['rpassword'])
            print('Name:',form.cleaned_data['email'])
    return render(request,'completeapp/signup.html',{'signup':form})
