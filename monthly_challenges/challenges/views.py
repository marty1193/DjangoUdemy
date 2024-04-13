from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index_jan(request):
    return HttpResponse("This works- January")


def index_feb(request):
    return HttpResponse("This works - February")



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

# def monthly_challenge(request, month_chosen):
#     if month_chosen.lower() == "january":
#         challenge_text = "This works- January"
#     elif month_chosen.lower() == "february":
#         challenge_text = "This works- February"
#     elif month_chosen.lower() == "march":
#         challenge_text = "This works- March"
#     else:
#         return HttpResponseNotFound("This Month is Not supported")
    
#     return HttpResponse(challenge_text)


monthly_challenge_dict={
    "january": "This is January Task : Read one Book ",
    "february": "This is February Task : Walk 1 km Daily",
    "March": "This is March Task : Walk 3 km Daily",
    "April": "This is April Task : Eat Apple Daily ",
    "May": "This is May Task : Watch Finance Shows",
    "June": "This is June Task : Walk 3 km Daily",
    "july": "This is july Task : Read one Book ",
    "August": "This is August Task : Walk 1 km Daily",
    "September": "This is September Task : Walk 3 km Daily",
    "October": "This is October Task : Read one Book ",
    "November": "This is November Task : Walk 1 km Daily",
    "December": "This is December Task : Walk 3 km Daily",
}
def monthly_challenge(request, month_chosen):
    try:
        if monthly_challenge_dict[month_chosen]:
            return HttpResponse(monthly_challenge_dict[month_chosen])
    except:
        return HttpResponseNotFound("Not Found Invalid Month")
