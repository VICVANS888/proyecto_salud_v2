from django.shortcuts import render

def intro_interface(request):
    return render(request, 'intro/intro_interface.html')



