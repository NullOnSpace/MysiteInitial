# Generated by Django 2.0.4 on 2018-06-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0020_auto_20180624_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liveroom',
            name='ownerid',
        ),
        migrations.AddField(
            model_name='liveroom',
            name='ownernn',
            field=models.CharField(default='Unknown', max_length=40),
            preserve_default=False,
        ),
    ]
