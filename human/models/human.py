import uuid
from django.db import models
from django.utils import timezone


class Human(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=55, blank=False)
    male = models.CharField(max_length=1, blank=False)
    number = models.IntegerField(max_length=12, unique=True)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    city = models.CharField(max_length=55)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        ordering = ["-created_at"]