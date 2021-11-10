from django.contrib import admin
from app.models import pf_projs

@admin.register(pf_projs)
class pf_projs_admin(admin.ModelAdmin):
    list_display = ("title", "author", "date_creation")