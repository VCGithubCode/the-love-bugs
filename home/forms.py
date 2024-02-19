from django import forms
from .models import Profile
from django.forms.fields import DateTimeField


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['name_one', 'name_two', 'location_one', 'location_two', 'status', 'datetime_field']
#         widgets = {
#             'datetime_field': forms.DateTimeInput(attrs={'type': 'datetime-local'})
#         }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name_one', 'name_two', 'location_one', 'location_two', 'status', 'datetime_field']
        widgets = {
            'datetime_field': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def clean(self):
        cleaned_data = super().clean()
        location_one = cleaned_data.get('location_one')
        location_two = cleaned_data.get('location_two')
        
        # Call the autocorrect API for location_one
        autocorrected_location_one, location_one_coords = self.autocorrect_location(location_one)
        cleaned_data['location_one'] = autocorrected_location_one
        cleaned_data['location_one_latitude'] = location_one_coords[0]
        cleaned_data['location_one_longitude'] = location_one_coords[1]
        
        # Call the autocorrect API for location_two
        autocorrected_location_two, location_two_coords = self.autocorrect_location(location_two)
        cleaned_data['location_two'] = autocorrected_location_two
        cleaned_data['location_two_latitude'] = location_two_coords[0]
        cleaned_data['location_two_longitude'] = location_two_coords[1]
        
        return cleaned_data

    def autocorrect_location(self, location):
        try:
            mapbox_access_token = os.getenv('GEOLOCATE_API_KEY')
            api_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{location}.json'
            payload = {'access_token': mapbox_access_token}
            response = requests.get(api_url, params=payload)
            
            if response.status_code == 200:
                data = response.json()
                features = data.get('features', [])
                if features:
                    # Get the coordinates from the first feature's center
                    center = features[0].get('center', [])
                    autocorrected_location = features[0].get('place_name', location)
                    return autocorrected_location, center
            return location, (None, None)
        except Exception as e:
            print(f"Error while autocorrecting location: {e}")
            return location, (None, None)
