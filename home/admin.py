from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name_one', 'name_two', 'location_one', 'location_two', 'status']

admin.site.register(Profile, ProfileAdmin)
