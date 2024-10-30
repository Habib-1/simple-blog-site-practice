from django.urls import path
from .import views
urlpatterns = [
    path('sign_up/',views.profile,name='profile')
]