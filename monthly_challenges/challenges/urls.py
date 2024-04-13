from django.urls import path
from . import views

# adding path details here
urlpatterns = [
    path("january", views.index)
    ]