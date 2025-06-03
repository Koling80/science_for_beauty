from django.shortcuts import render



# Create your views here.


def home_page(request):
    return render(request, 'science_for_beauty.html')