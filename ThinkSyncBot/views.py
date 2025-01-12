from django.shortcuts import render, HttpResponse
from .forms import NameForm

# Create your views here.
def get_name(request):
    if request.method == "GET":
        form = NameForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            company = form.cleaned_data["company"]
            meet = form.cleaned_data["link"]
            
            print(name)
            print(company)
            print(meet)
        else:
            form = NameForm()

    return render(request, "base.htm")

def base(request):
    return render(request, "base.htm")
