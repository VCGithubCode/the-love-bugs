from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/profile_view', views.profile_view, name='profile_view'),
]
