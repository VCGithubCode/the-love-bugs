from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

def index(request):
    profiles = Profile.objects.all()

    # List to store marker coordinates for location_one and location_two
    markers = []

    # Iterate through profiles and geocode location_one and location_two
    for profile in profiles:
        # Geocode location_one
        location_one = profile.location_one
        coordinates_one = geocode_location(location_one)
        if coordinates_one:
            markers.append({'name': profile.name_one, 'coordinates': coordinates_one})

        # Geocode location_two
        location_two = profile.location_two
        coordinates_two = geocode_location(location_two)
        if coordinates_two:
            markers.append({'name': profile.name_two, 'coordinates': coordinates_two})

    return render(request, 'home/index.html', {'markers': markers})

def geocode_location(location):
    # Use a geocoding service to obtain coordinates for the location
    # This function should handle the API request and return coordinates
    # Example: Use Mapbox Geocoding API, Google Geocoding API, etc.
    # Replace YOUR_API_KEY with your actual API key
    api_key = 'pk.eyJ1IjoidmNvbmxpbmVlZHVjYXRpb24iLCJhIjoiY2xzcWgwOWM4MDM3bDJzczB4cHc3OWc4MCJ9.0hoLrOXYccgLBU0HY5JGpA'
    url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{location}.json?access_token={api_key}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'features' in data and data['features']:
                coordinates = data['features'][0]['geometry']['coordinates']
                return coordinates[::-1]  # Reversing the coordinates to [latitude, longitude]
    except Exception as e:
        print(f"Error geocoding location: {e}")
    
    return None
    return render(request, 'home/index.html', {'profiles': profiles})



def contact(request):
    """ A view to return the contact page """

    return render(request, 'home/contact.html')

def test(request):
    """ A view to return the contact page """

    return render(request, 'home/test.html')



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
    if Profile.objects.filter(user=request.user).exists():
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

@login_required
def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('profile')

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'home/edit_profile.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.delete()
        request.user.delete()
        logout(request)
        return redirect('home')
    else:
        return render(request, 'home/delete_profile_confirmation.html')