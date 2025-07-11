# Generated by Django 5.2.1 on 2025-06-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_productintake_application_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productintake',
            name='application_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('completed_documentation', 'Completed Documentation'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=30, verbose_name='Application Status'),
        ),
        migrations.AlterField(
            model_name='productintake',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=10),
        ),
    ]
