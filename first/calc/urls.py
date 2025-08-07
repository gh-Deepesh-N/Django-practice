from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('travello.urls')),  # Home view for the calculator app
    path('add/', views.add, name='add')  # Example of another view
]
