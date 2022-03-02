from django.shortcuts import render
from django.views.generic import ListView

def contact(request):
	return render(request,'contact/contact.html')