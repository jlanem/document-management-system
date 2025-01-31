from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    reg_date = models.DateField(help_text="The date of Company incoparation")
    directors = models.TextField(help_text="List of directors, separated by commas")
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class DocumentType(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="document type name")
    document_issuer = models.CharField(max_length=255, help_text="The Authority issuing the document")

    def __str__(self):
        return self.name

class Document(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="documents")
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, null=True, related_name="documents")
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")
    registration_date = models.DateField()
    expiration_date = models.DateField()
    validity_period = models.CharField()

    def __str__(self):
    	return f"{self.name} ({self.company.name})"
        # return f"{self.name} ({self.document_type.name} - {self.company.name})"
