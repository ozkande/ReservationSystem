# Generated by Django 2.1.5 on 2019-02-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.CharField(max_length=10)),
                ('table_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='branch',
        ),
    ]
