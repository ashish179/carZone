from django.shortcuts import render
from .models import Team
# Create your views here.

def home(req):

    teams=Team.objects.all() 
    data={'teams':teams,}
    return render(req,'pages/home.html',data)

def about(req):

    teams= Team.objects.all()
    data={'teams':teams}
    return render(req,'pages/about.html',data)

def services(req):


    return render(req,'pages/services.html')
def contact(req):


    return render(req,'pages/contact.html')