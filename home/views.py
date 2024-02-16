from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to return the index page """    
    
    return render(request, 'home/index.html')



def profile(request):
    """ A view to return the users profile """

    return render(request, 'home/profile.html')