from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('page/<int:menu_item_id>/', views.main_list, name='main_list')
]