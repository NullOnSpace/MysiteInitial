# Generated by Django 2.0.4 on 2018-06-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20180605_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='bid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='uid',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
