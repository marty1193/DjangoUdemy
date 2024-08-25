from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def review(request):
    if request.method =="GET":
        return render(request, "reviews/review.html",{
                          "has_error":False
            })
    
    elif request.method == "POST":
        entered_username = request.POST['username']
        print(entered_username)
        if entered_username =="":
            return render(request, "reviews/review.html",{
                          "has_error":True
            })
        return HttpResponseRedirect("/thank-you")


def thank_user(request):
    return render(request, "reviews/thankyou.html")
