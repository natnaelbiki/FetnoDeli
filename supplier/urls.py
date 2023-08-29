from django.urls import path
from .views import CreateShop, UpdateShop

urlpatterns = [
	path('new_shop/', CreateShop.as_view(), name='new_shop'),
	path('update_shop/<int:pk>/', UpdateShop.as_view(), name='update_shop'),
]