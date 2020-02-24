# Generated by Django 3.0.2 on 2020-02-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0006_auto_20200201_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='external_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='external_link_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_region_primary',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_region_secondary',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]