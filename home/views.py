from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """ A view to return the index page """    
    
    return render(request, 'home/index.html')


def contact(request):
    """ A view to return the contact page """

    return render(request, 'home/contact.html')



def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')

def profile_view(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        context = {'profile': profile}
        return render(request, 'home/profile_view.html', context)
    else:
        return redirect('profile')


@login_required
def profile(request):
    if request.user.profile:
        return redirect('profile_view')

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_view')
    else:
        form = ProfileForm()
    return render(request, 'home/profile.html', {'form': form})

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('profile_view')
#     else:
#         form = ProfileForm()
#     return render(request, 'home/profile.html', {'form': form})

