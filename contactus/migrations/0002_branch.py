# Generated by Django 2.1.5 on 2019-02-26 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=250)),
                ('branch_address', models.CharField(max_length=500)),
                ('branch_city', models.CharField(max_length=100)),
                ('branch_email', models.CharField(max_length=250)),
                ('branch_phone_number', models.CharField(max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactus.Company')),
            ],
        ),
    ]