# Generated by Django 5.0.1 on 2024-01-17 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patagonia', '0003_portfolio_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='showeight',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='showfive',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='showseven',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='showsix',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
