from django import template
from django.utils.safestring import mark_safe
from app.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(current_item_id=None):
    root_menu_items = MenuItem.objects.filter(parent=None)
    return mark_safe(draw_items(root_menu_items, current_item_id))

def draw_items(items, current_item_id, in_path_to_current=False):
    html = '<ul class="menu-root">' if not in_path_to_current else '<ul class="submenu">'
    for item in items:
        css_class = 'menu-item'
        if item.id == current_item_id:
            css_class += ' selected'
        
        children_html = ''
        if item.children.exists():
            css_class += ' has-children'
            children_html = draw_items(item.children.all(), current_item_id, True)
            if 'selected' in children_html:
                css_class += ' selected'
        
        html += f'<li class="{css_class}"><a href="{item.get_absolute_url()}">{item.name}</a>'
        html += children_html
        html += '</li>'
    html += '</ul>'
    return html
