from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string

# Custom User
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50, blank=True, null=True)
    # company_name = models.CharField(max_length=250, blank=True, null=True)
    # phone_number = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    

# New FDA Application
class FDAApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_review', 'In Review'),
        ('completed_documentation', 'Completed Documentation'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fda_applications')
    business_certificate = models.FileField(upload_to='fda/business_certificates/')
    business_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    products = models.TextField()
    logo = models.ImageField(upload_to='fda/logos/', null=True, blank=True)
    lab_results = models.FileField(upload_to='fda/lab_results/', null=True, blank=True)
    product_labels = models.FileField(upload_to='fda/product_labels/', null=True, blank=True)
    food_handler_cert = models.FileField(upload_to='fda/food_handler_certs/', null=True, blank=True)
    process_description = models.TextField(null=True, blank=True)
    voice_note = models.FileField(upload_to='fda/voice_notes/', null=True, blank=True)
    facility_video = models.FileField(upload_to='fda/facility_videos/', null=True, blank=True)
    items_equipment = models.TextField()
    staff_roles = models.TextField()
    application_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.business_name} - {self.user.email}"


# New Business Certificate Registration
class BusinessCertificateApplication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    company_name = models.CharField(max_length=100)
    nature_of_business = models.CharField(max_length=100)
    postal_address = models.TextField()
    contact_number_one = models.CharField(max_length=15)
    contact_number_two = models.CharField(max_length=15)
    company_email = models.CharField(max_length=50)
    company_building_number = models.CharField(max_length=10)
    company_landmark = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    company_gps_address = models.CharField(max_length=100)
    ghana_card_number = models.CharField(max_length=100)
    tin_number = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.company_name} - {self.company_email}"
    