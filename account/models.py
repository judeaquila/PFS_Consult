from django.db import models
from django.contrib.auth.models import AbstractUser
from services.utils import generate_custom_id

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
    

# FDA REQUIREMENTS
class FDAFoodRequirement(models.Model):
    HELP_CHOICES = [
        ('have', 'I have this'),
        ('need_help', 'I need help from PFS'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fda_food_requirements')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    food_handlers_card = models.CharField(max_length=10, default='', choices=YES_NO_CHOICES, verbose_name="Food Handler's Card")
    product_lab_test = models.CharField(max_length=10, default='', choices=HELP_CHOICES, verbose_name='Product Lab Test')
    product_label = models.CharField(max_length=10, default='', choices=HELP_CHOICES, verbose_name='Product Label')
    business_certificate = models.CharField(max_length=10, default='', choices=HELP_CHOICES, verbose_name='Business Certificate')

    product_pictures = models.CharField(max_length=10, default='', choices=YES_NO_CHOICES, verbose_name='I have Product Pictures')
    product_samples = models.CharField(max_length=10, default='', choices=YES_NO_CHOICES, verbose_name='I have Product Samples')

    def __str__(self):
        return f"FDA Requirements for {self.user.first_name} - {self.submitted_at.strftime('%Y-%m-%d')}"
    

class FDAEateriesRequirement(models.Model):
    HELP_CHOICES = [
        ('have', 'I have this'),
        ('need_help', 'I need help from PFS'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fda_eateries_requirements')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    food_handlers_card = models.CharField(max_length=10, default='', choices=YES_NO_CHOICES, verbose_name="Food Handler's Card")
    list_of_recipes = models.CharField(max_length=10, default='', choices=YES_NO_CHOICES, verbose_name='List of Recipes')
    recipe_preparation_steps = models.CharField(max_length=10, default='', choices=HELP_CHOICES, verbose_name="Recipe Preparation Steps")
    business_certificate = models.CharField(max_length=10, default='', choices=HELP_CHOICES, verbose_name='Business Certificate')

    def __str__(self):
        return f"FDA Requirements for {self.user.first_name} - {self.submitted_at.strftime('%Y-%m-%d')}"
    

class FDACosmeticsRequirement(models.Model):
    HELP_CHOICES = [
        ('have', 'I have this'),
        ('need_help', 'I need help from PFS'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fda_cosmetics_requirements')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    product_label = models.CharField(max_length=10, default='', choices=HELP_CHOICES, verbose_name='Product Label')
    business_certificate = models.CharField(max_length=10, default='', choices=HELP_CHOICES, verbose_name='Business Certificate')
    product_pictures = models.CharField(max_length=10, default='', choices=YES_NO_CHOICES, verbose_name='I have Product Pictures')
    product_samples = models.CharField(max_length=10, default='', choices=YES_NO_CHOICES, verbose_name='I have Product Samples')    
    

# New FDA Application
class FDAApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_review', 'In Review'),
        ('completed_documentation', 'Completed Documentation'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    PAYMENT_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fda_applications')
    custom_id = models.CharField(max_length=30, unique=True, blank=True)
    business_certificate = models.FileField(upload_to='fda/business_certificates/')
    business_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    products = models.TextField()
    logo = models.ImageField(upload_to='fda/logos/', null=True, blank=True)
    # lab_results = models.FileField(upload_to='fda/lab_results/', null=True, blank=True)
    product_labels = models.FileField(upload_to='fda/product_labels/', null=True, blank=True)
    food_handlers_card = models.FileField(upload_to='fda/food_handler_certs/', null=True, blank=True)
    process_description = models.TextField(null=True, blank=True)
    voice_note = models.FileField(upload_to='fda/voice_notes/', null=True, blank=True)
    # facility_video = models.FileField(upload_to='fda/facility_videos/', null=True, blank=True)
    # items_equipment = models.TextField()
    # staff_roles = models.TextField()

    application_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='unpaid')

    def save(self, *args, **kwargs):
        if not self.custom_id:
            self.custom_id = generate_custom_id('FDA-Prod')
        super().save(*args, **kwargs)


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

    PAYMENT_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
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
    custom_id = models.CharField(max_length=30, unique=True, blank=True)
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
    ghana_card_front = models.ImageField(upload_to='business_cert/gc/')
    ghana_card_back = models.ImageField(upload_to='business_cert/gc/')
    tin_number = models.CharField(max_length=100)
    application_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='unpaid')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
            if not self.custom_id:
                self.custom_id = generate_custom_id('BZ-Cert')
            super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.business_name} - {self.company_email}"


class LLCBusinessCertificateApplication(models.Model):
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
        ('non_governmental_organization', 'Non-Governmental Organization'),
        ('limited_liability_company', 'Limited Liability Company'),
    ]

    PAYMENT_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
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
    custom_id = models.CharField(max_length=30, unique=True, blank=True)
    tin_number = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    landmark = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    gps_address = models.CharField(max_length=100)
    postal_address = models.TextField()

    business_name = models.CharField(max_length=100)
    nature_of_business = models.CharField(max_length=100)
    type_of_business = models.CharField(max_length=100, choices=BUSINESS_TYPE_CHOICES)
    business_postal_address = models.TextField()
    business_contact_number_one = models.CharField(max_length=15)
    business_contact_number_two = models.CharField(max_length=15, blank=True, null=True)
    business_email = models.EmailField(max_length=100)
    business_building_number = models.CharField(max_length=10)
    business_landmark = models.CharField(max_length=255)
    business_area = models.CharField(max_length=100)
    business_district = models.CharField(max_length=100)
    business_gps_address = models.CharField(max_length=100)
    ghana_card_number = models.CharField(max_length=100)
    ghana_card_front = models.ImageField(upload_to='business_cert/gc/')
    ghana_card_back = models.ImageField(upload_to='business_cert/gc/')
    business_tin_number = models.CharField(max_length=100)
    
    application_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='unpaid')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
            if not self.custom_id:
                self.custom_id = generate_custom_id('BZ-Cert')
            super().save(*args, **kwargs)


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