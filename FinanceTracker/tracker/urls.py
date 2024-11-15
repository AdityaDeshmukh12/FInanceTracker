from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page with form and transactions list
]
