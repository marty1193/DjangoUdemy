from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index_jan(request):
    return HttpResponse("This works- January")


def index_feb(request):
    return HttpResponse("This works - February")


def monthly_challenge(request, month_chosen):
    if month_chosen.lower() == "january":
        challenge_text = "This works- January"
    elif month_chosen.lower() == "february":
        challenge_text = "This works- February"
    elif month_chosen.lower() == "march":
        challenge_text = "This works- March"
    else:
        return HttpResponseNotFound("This Month is Not supported")
    
    return HttpResponse(challenge_text)



def monthly_challenge_by_num(request, month_chosen):
    if month_chosen== 1:
        challenge_text = "This works- January"
    elif month_chosen== 2:
        challenge_text = "This works- February"
    elif month_chosen== 3:
        challenge_text = "This works- March"
    else:
        return HttpResponseNotFound("This Month is Not supported")
    
    return HttpResponse(challenge_text)
