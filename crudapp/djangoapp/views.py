from django.shortcuts import render


def index(request):
    return render(request, "djangoapp/index.html",
                  {'title': 'All Django Project'})
# Create your views here.
