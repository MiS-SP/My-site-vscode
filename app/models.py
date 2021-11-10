"""
Definition of models.
"""

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class pf_projs(models.Model):
    title = models.CharField(max_length=60),
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        )
    body = models.TextField()
