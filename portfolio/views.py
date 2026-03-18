from django.shortcuts import render

def home(request):
    context = {
        'name': 'YONAS SOLOMON',
        'title': 'Software Engineering Student',
    }
    return render(request, 'portfolio/home.html', context)