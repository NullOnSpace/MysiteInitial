# Generated by Django 2.0.4 on 2018-06-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20180605_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='lastaccess',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
