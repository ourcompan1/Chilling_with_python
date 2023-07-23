from django.shortcuts import render


def main(request):
    return render(request, 'burgos/homepage.html', {})
