# Generated by Django 2.0.4 on 2018-06-12 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_auto_20180610_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='cicon',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='cname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]