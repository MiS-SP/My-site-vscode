"""
Definition of models.
"""

from django.db import models

class pf_projs(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    body = models.TextField(null=True)
    date_creation = models.DateField(auto_now_add=True)