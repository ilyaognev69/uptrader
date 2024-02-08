from django.shortcuts import render, get_object_or_404
from .models import Page
# Create your views here.

def home(request):
	return render(request, 'app/base.html')

def main_list(request, menu_item_id):
	page = get_object_or_404(Page, menu_item_id=menu_item_id)
	return render(request, 'app/main.html', {'page':page})