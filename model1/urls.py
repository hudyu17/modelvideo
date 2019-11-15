from django.urls import path
from . import views

urlpatterns = [ # create one url pattern for each page
    path('', views.home, name = 'home'),
    path('results', views.results, name = 'results')
    ]