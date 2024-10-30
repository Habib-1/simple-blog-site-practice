from django.urls import path
from . import views
urlpatterns = [
    path('add_categories/',views.addCategory,name='add_category'),
]
