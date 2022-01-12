from django.contrib import admin
from app.models import pf_proj

@admin.register(pf_proj)
class pf_projs_admin(admin.ModelAdmin):
    list_display = ("title", "author", "date_creation")