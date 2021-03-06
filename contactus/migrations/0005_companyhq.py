# Generated by Django 2.1.5 on 2019-02-26 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0004_auto_20190226_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyHQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hq_address', models.CharField(max_length=500)),
                ('hq_city', models.CharField(max_length=100)),
                ('hq_country', models.CharField(max_length=50)),
                ('company_email', models.CharField(max_length=250)),
                ('company_phone_number', models.CharField(max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactus.Company', unique=True)),
            ],
        ),
    ]
