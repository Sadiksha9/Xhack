from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def scan(request):
    return render(request, 'scan.html')

def contact(request):
    return render(request, 'contact.html')


def complain(request):
    return render(request, 'complain.html')