# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
ROLE = (
	('su', 'Supplier'),
    ('st', 'Stuff'),
    ('de', 'Delivery'),
    ('cu', 'Customer'),
    )


class CustomUser(AbstractUser):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    role = models.CharField(choices=ROLE, max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
