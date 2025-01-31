from django.contrib import admin

from .models import Company, Document, DocumentType

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class DocumentInline(admin.TabularInline):  # or admin.StackedInline for a different UI
    model = Document
    extra = 1

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number")
    search_fields = ("name", "email", "directors")
    inlines = [DocumentInline]

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "expiration_date")
    list_filter = ("expiration_date",)
    search_fields = ("name", "company__name")
