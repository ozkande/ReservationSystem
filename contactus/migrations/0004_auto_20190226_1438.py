# Generated by Django 2.1.5 on 2019-02-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0003_customerservicehours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerservicehours',
            name='company_open_days_end',
        ),
        migrations.RemoveField(
            model_name='customerservicehours',
            name='company_open_days_start',
        ),
        migrations.AddField(
            model_name='customerservicehours',
            name='company_open_days',
            field=models.CharField(default='Monday', max_length=10),
        ),
    ]
