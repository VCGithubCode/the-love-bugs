from django.shortcuts import render, redirect
from .forms import ProfileForm

# Create your views here.
def index(request):
    """ A view to return the index page """    
    
    return render(request, 'home/index.html')



# def profile(request):
#     """ A view to return the users profile """

#     return render(request, 'home/profile.html')



def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = ProfileForm()
    return render(request, 'home/profile.html', {'form': form})