from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView


# Create your views here.
def homePageView(request):
    return render(request, "home.html", {
        "my_numbers":[1, 2, 3, 4, 5, 6],
        "first_name": "Momona",
        "last_name": "Wada"
    })

def aboutPageView(request):
    return render(request, "about.html")

def momonaPageView(request):
    return render(request, "momona.html")

def homePost(request):
    # create variable to store choice that is recognized through entire function
    choice = -999

    try:
        # Extract value from request object by control name.
        current_choice = request.POST["choice"]

        # Crude debugging effort
        print(f"*** Years work experience: {current_choice}")
        choice = int(current_choice)

    except:
        return render(request, "home.html", {
            "error_message": "*** The choice was missing. Please try again ***",
            "my_numbers": [1, 2, 3, 4, 5, 6]
        })
    else:
        # always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a user hits the Back button
        return HttpResponseRedirect(reverse("results", args=(choice,)))


def results(request, choice):
    print("*** Inside results()")
    return render(request, "result.html", {"choice": choice})