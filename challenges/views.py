from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat no meat for the entire montn!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes very day!",
    "april": "Eat no meat for the entire montn!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes very day!",
    "july": "Eat no meat for the entire montn!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes very day!",
    "october": "Eat no meat for the entire montn!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes very day!"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())

        if month > len(months):
            return HttpResponseNotFound("Invalid month")
        
        redirect_month = months[month - 1]
        return HttpResponseRedirect("/challenges/" + redirect_month)
    except:
        return HttpResponseNotFound("This month is not supported.")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported.")
