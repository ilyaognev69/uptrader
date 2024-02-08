from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MenuItem, Page

@receiver(post_save, sender=MenuItem)
def create_update_menu_item_page(sender, instance, created, **kwargs):
    if created:
        Page.objects.create(menu_item=instance, title=instance.name, content='')
    else:
        Page.objects.filter(menu_item=instance).update(title=instance.name)
