from django.shortcuts import render
from . models import Events


# Create your views here.
def home(request):
    events=Events.objects.all()
    return render(request,'home.html',{'Events':events})

def add_events(request):
    if request.POST:
        event_name=request.POST.get('event_name')
        event_description=request.POST.get('event_description')
        Events_obj=Events(event_name=event_name,event_description=event_description)
        Events_obj.save()

    return render(request,'add_events.html')