# Generated by Django 4.1.4 on 2023-05-01 09:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pythonProject', '0006_heritagedetails_photo2_heritagedetails_photo3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='heritagedetails',
            name='SuggestedPhoto1',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
        migrations.AddField(
            model_name='heritagedetails',
            name='SuggestedPhoto2',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
        migrations.AddField(
            model_name='heritagedetails',
            name='SuggestedPlaceName1',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heritagedetails',
            name='SuggestedPlaceName2',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
