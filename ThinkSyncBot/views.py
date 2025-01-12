from django.shortcuts import render, HttpResponse
from .forms import NameForm
from .meetjoinattempt2 import Bot

def get_name(request):
    if request.method == "GET":
        form = NameForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            company = form.cleaned_data["company"]
            meet = form.cleaned_data["link"]
            
            bot_instance = Bot()
            bot_instance.runBot(meet_link=meet)
        else:
            form = NameForm()

    return render(request, "base.htm")

def base(request):
    return render(request, "base.htm")
