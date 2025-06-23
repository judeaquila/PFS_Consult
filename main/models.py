from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# FAQs
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = CKEditor5Field(config_name='default')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question

