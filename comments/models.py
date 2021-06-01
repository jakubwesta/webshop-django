from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.utils import timezone
from django.urls import reverse

import uuid
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from webshop import settings


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    
    content = models.CharField(max_length=5000, blank=False)

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
