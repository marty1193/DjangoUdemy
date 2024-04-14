from django.urls import path
from . import views

# adding path details here
urlpatterns = [
    # path("january", views.index_jan),
    # path("february", views.index_feb),
    # Here the value inside <> act as a keyword argument for the corresponding view i.e monthly_challenge
    path("<int:month_chosen>", views.monthly_challenge_by_num),
    path("<str:month_chosen>", views.monthly_challenge),
]
