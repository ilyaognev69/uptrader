# Generated by Django 4.2.9 on 2024-02-08 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_menuitem_url_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='url_name',
        ),
    ]
