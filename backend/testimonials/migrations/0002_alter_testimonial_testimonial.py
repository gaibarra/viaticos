# Generated by Django 4.0.6 on 2023-02-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.CharField(max_length=400),
        ),
    ]
