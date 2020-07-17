from django.urls import path 
# from home import views
from home.views import HomeView
from . import views



urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    
]
