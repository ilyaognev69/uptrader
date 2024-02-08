from .models import MenuItem
from django.urls import resolve

def menu_context_processor(request):
    menu_item_id = None
	
    if 'menu_item_id' in request.resolver_match.kwargs:
        menu_item_id = request.resolver_match.kwargs['menu_item_id']
    
    return {'current_item_id': menu_item_id}

