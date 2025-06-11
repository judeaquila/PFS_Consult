from django.db import models

class ProductIntake(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('new', 'New Product Idea'),
        ('improvement', 'Improvement of Existing Product'),
    ]

    GOALS_CHOICES = [
        ('shelf_life', 'Longer shelf life'),
        ('unique_taste', 'Unique taste'),
        ('healthier', 'Healthier version'),
        ('cost_reduction', 'Cost reduction'),
        ('novel_format', 'Novel format (e.g., instant, ready-to-eat)'),
        ('other', 'Other'),
    ]

    TARGET_MARKET_CHOICES = [
        ('children', 'Children'),
        ('adults', 'Adults'),
        ('vegans', 'Vegans'),
        ('fitness', 'Fitness enthusiasts'),
        ('diabetics', 'Diabetics'),
        ('mass', 'Mass market'),
        ('other', 'Other'),
    ]

    PACKAGING_CHOICES = [
        ('sachet', 'Sachet'),
        ('jar', 'Jar/Bottle'),
        ('box', 'Box'),
        ('pouch', 'Stand-up pouch'),
        ('custom', 'Custom'),
    ]

    MARKET_TESTING_CHOICES = [
        ('good', 'Yes, with good results'),
        ('need_more', 'Yes, but need more data'),
        ('not_yet', 'No, not yet'),
        ('planning', 'Planning to do so'),
    ]

    type_of_product = models.CharField(max_length=200, verbose_name='Type of Product')
    is_new_or_improvement = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES, verbose_name='Is this a New Idea or Improvement?')
    goals = models.JSONField(default=list, verbose_name='What is/are your goal(s) for the Product?')
    other_goal = models.CharField(max_length=200, blank=True, verbose_name='Other')
    ingredient_or_dietary_notes = models.TextField(blank=True, verbose_name='Do you have a Preferred Ingredient List or any Dietary Restrictions?')
    target_market = models.JSONField(default=list, verbose_name='Target Market')
    other_target_market = models.CharField(max_length=200, blank=True, verbose_name='Other')
    market_existence = models.CharField(max_length=20, choices=[('yes', 'Yes'), ('no', 'No'), ('not_sure', 'Not Sure')], verbose_name='Are there similar products already on the market?')
    packaging_style = models.JSONField(default=list, verbose_name='What Packaging Style are you envisioning?')
    custom_packaging = models.CharField(max_length=200, blank=True, verbose_name='Custom')
    expected_launch_date = models.DateField(verbose_name='Expected Launch Date')
    market_testing_feedback = models.CharField(max_length=20, choices=MARKET_TESTING_CHOICES, verbose_name='Have you done any Market Testing or Consumer Feedback?')

    def __str__(self):
        return self.type_of_product


class PaymentAccess(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    has_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {'Paid' if self.has_paid else 'Unpaid'}"