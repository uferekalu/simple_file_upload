from django.contrib import admin
from .models import Document

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('description', 'document', 'uploaded_at')
    search_fields = ['description']

admin.site.register(Document, DocumentAdmin)
