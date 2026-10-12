from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    'january': "Learn how to do a backflip.",
    'february': "Eat only one meal a day.",
    'march': "Perform a clean rep pullup.",
    'april': "Drink 5L of water every day.",
    'may': "Perform a song on an instrument you never played before.",
    'june': "Learn a video editing software.",
    'july': "Name and describe a different emotion each day in a diary.",
    'august': "Sleep, eat, and do daily tasks at the exact same time every single day.",
    'september': "Pick a martial art and start doing it, either at home with a sandbag or classes.",
    'october': "Get as flexible as you can in one month.",
    'november': "Understand the true nature of humans.",
    'december': "Build the empire."
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("This ain't a month!!!!")
    
    redirect_month = months[month-1]
    
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january

    return HttpResponseRedirect(redirect_path)



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })

    except:
        return HttpResponseNotFound("<h1>This ain't a month!!!!</h1>")
