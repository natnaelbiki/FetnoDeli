from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Shop

class CreateShop(CreateView):
	model = Shop
	template_name = 'supplier/create_shop.html'
	fields = ['name', 'desc', 'location']

class UpdateShop(UpdateView):
	model = Shop
	template_name = 'supplier/update_shop.html'
	fields = ['name', 'desc', 'location']