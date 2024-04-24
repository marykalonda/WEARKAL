from django.shortcuts import render

# Create your views here.
def home(request):    
    return render(request, 'pages/home.html')

def view_name(request):    
    return render(request, 'pages/apropos.html')
    
def view_nam(request):    
    return render(request, 'pages/boutique.html')

def view_na(request):    
    return render(request, 'pages/contact.html')

def view_n(request):    
    return render(request, 'pages/voirmodel.html')


