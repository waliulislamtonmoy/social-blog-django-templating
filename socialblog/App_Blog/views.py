from django.shortcuts import render



# Create your views here.

from django.views.generic import ListView


# class HomeView(ListView):
#     template_name='App_Blog/Home.html'


    
def HomeView(request):
    return render(request,"App_Blog/Home.html")