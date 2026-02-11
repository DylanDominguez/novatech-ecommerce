from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'novatech/index.html', context)