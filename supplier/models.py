from django.db import models
from accounts.models import CustomUser


class Shop(models.Model):
	owner = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
	name = models.CharField(max_length = 30, blank=False)
	location = models.CharField(max_length = 30, blank=False)
	desc = models.CharField(max_length=250, blank=False)

	def __str__(self):
		return self.name

# Create your models here.
