from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
	name = models.CharField(max_length=100)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('app:main_list', kwargs={'menu_item_id':self.id})
	
class Page(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	menu_item = models.OneToOneField(MenuItem, on_delete=models.CASCADE, related_name='page')

	def __str__(self):
		return self.title