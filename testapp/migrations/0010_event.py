# Generated by Django 2.0.4 on 2018-06-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_band_lastaccess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=12)),
                ('oid', models.CharField(max_length=12)),
                ('msgtype', models.CharField(db_column='type', max_length=20)),
                ('roomid', models.IntegerField()),
                ('optime', models.IntegerField()),
                ('rint', models.IntegerField()),
                ('rstr', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]
