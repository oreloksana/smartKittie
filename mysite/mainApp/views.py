from django.shortcuts import render

def index(request):
    return render( request, 'mainApp/homePage.html')

def contact(request):
    return render( request, 'mainApp/basic.html', {'values':['Если у Вас остались вопросы,задайте их по телефону','+380638745029']})