from django.shortcuts import render

def page1(request):
    return render(request, 'gadjetapp/gadjet.html', {})
