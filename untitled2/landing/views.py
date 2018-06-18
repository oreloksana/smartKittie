from django.shortcuts import render


def landing(request):
    name = "Мамочка"
    current_day = "27.02.2018"
    return render(request, 'landing/landing.html', locals())