from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Last Name')
    business_name = models.CharField(max_length=250, verbose_name='Business/Company Name')
    phone_number = models.CharField(max_length=30, verbose_name='Phone Number')
    whatsapp_number = models.CharField(max_length=30, verbose_name='Whatsapp Number')
    instagram_handle = models.CharField(max_length=30, blank=True, verbose_name='Instagram Handle')
    facebook_handle = models.CharField(max_length=30, blank=True, verbose_name='Facebook Profile')
    profile_photo = models.ImageField(upload_to='users/profile_photos/', null=True, blank=True, verbose_name='Profile Photo')
    bio = models.TextField(blank=True, verbose_name='Bio')
    x_handle = models.CharField(max_length=30, blank=True, verbose_name='X (Formerly Twitter) Handle')
    linkedin_handle = models.CharField(max_length=30, blank=True, verbose_name='LinkedIn Profile')

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
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
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
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_review', 'In Review'),
        ('completed_documentation', 'Completed Documentation'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    BUSINESS_TYPE_CHOICES = [
        ('sole_proprietorship', 'Sole Proprietorship'),
        ('non_governmental_organization', 'Non-Governmental Organization'),
        ('limited_liability_company', 'Limited Liability Company'),
    ]
        
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    marital_status = models.CharField(max_length=100, choices=MARITAL_STATUS_CHOICES)
    place_of_birth = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    contact_number_one = models.CharField(max_length=15)
    contact_number_two = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100)

    business_name = models.CharField(max_length=100)
    nature_of_business = models.CharField(max_length=100)
    type_of_business = models.CharField(max_length=100, choices=BUSINESS_TYPE_CHOICES)
    postal_address = models.TextField()
    company_email = models.EmailField(max_length=100)
    company_building_number = models.CharField(max_length=10)
    company_landmark = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    company_gps_address = models.CharField(max_length=100)
    ghana_card_number = models.CharField(max_length=100)
    tin_number = models.CharField(max_length=100)
    application_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.business_name} - {self.company_email}"



# USER ACTIVITY
class UserActivity(models.Model):
    ACTIVITY_CHOICES = [
    ('login', 'Logged In'),
    ('logout', 'Logged Out'),
    ('profile_update', 'Profile Updated'),
    ('message_sent', 'Message Sent'),
    ('message_received', 'Message Received'),
    ('submit_product', 'Submitted Product Application'),
    ('submit_facility', 'Submitted Facility Application'),
    ('submit_business', 'Submitted Business Certificate Application'),
    ('status_changed', 'Application Status Updated'),
]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.activity_type} at {self.timestamp}"