# Generated by Django 2.0.4 on 2018-06-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_auto_20180605_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='bdlv',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='band',
            name='bid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='band',
            name='uid',
            field=models.CharField(max_length=12),
        ),
    ]