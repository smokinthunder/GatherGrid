from django.shortcuts import render,redirect
from . models import Events
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin ,logout as authlogout,authenticate,get_user
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def home(request):
    events=Events.objects.all()
    return render(request,'home.html',{'Events':events})

@login_required(login_url='login')
def add_events(request):
    if request.POST:
        event_name=request.POST.get('event_name')
        event_description=request.POST.get('event_description')
        event_organiser=get_user(request).username
        Events_obj=Events(event_name=event_name,event_description=event_description,event_organiser=event_organiser)
        Events_obj.save()
    return render(request,'add_events.html')

def login(request):
    if request.POST:
        user_name= request.POST.get('user_name')
        password= request.POST.get('password')
        user=authenticate(username=user_name,password=password)
        if user:
            print (user)
            authlogin(request,user)
            return redirect('home')

        


    return render(request,'login.html')
def logout(request):
    authlogout(request)
    return redirect ('login')

def signup(request):
    user=None
    if request.POST:
        first_name= request.POST.get('first_name')
        second_name= request.POST.get('second_name')
        email= request.POST.get('email')
        user_name= request.POST.get('user_name')
        password= request.POST.get('password')
        user=User.objects.create_user(username=user_name,email=email,password=password,first_name=first_name,last_name=second_name,)
    return render(request,'signup.html',{'user':user})

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html',{'user':get_user(request)})

@login_required(login_url='login')
def my_events(request):
    events=Events.objects.filter(event_organiser=get_user(request).username)
    return render(request,'myevents.html',{'Events':events})