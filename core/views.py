from django.shortcuts import render
from .models import Contact, contacts

# Create your views here.
def index(request):
    return render(request, 'main_page.html')

def get_contacts(request):
    return render(request, 'contacts.html', {'contacts': contacts})