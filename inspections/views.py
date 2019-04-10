from django.shortcuts import render

# Create your views here.
def index( request ):
    return render( request, 'hestia/index.html' )

def about( request ):
    return render( request, 'hestia/about.html' )
    
def contact( request ):
    return render( request, 'hestia/contact.html' )
    
def home( request ):
    return render( request, 'inspections/home.html' )

