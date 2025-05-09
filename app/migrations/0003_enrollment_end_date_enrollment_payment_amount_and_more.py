# Generated by Django 5.0.6 on 2024-07-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_enrollment_membershipplan_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='payment_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='payment_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='join_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
