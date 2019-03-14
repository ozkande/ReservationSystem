from django.db import models

# Create your models here.


from django.db import models
from datetime import datetime


class Company(models.Model):
    company_name = models.CharField(max_length= 250)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = 'companies'


class Branch(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    branch_name = models.CharField(max_length= 250)
    branch_address = models.CharField(max_length=500)
    branch_city = models.CharField(max_length=100)
    branch_email = models.CharField(max_length=250)
    branch_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.branch_name

    class Meta:
        verbose_name_plural = 'branches'


class CustomerServiceHours(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    company_open_hours_start = models.CharField(max_length=10)
    company_open_hours_end = models.CharField(max_length=10)
    company_open_days = models.CharField(max_length=10, default='Monday')

    class Meta:
        verbose_name_plural = 'Customer Service Hours'

    def __str__(self):
        return self.company_open_days +  " " + self.company_open_hours_start + " " + self.company_open_hours_end


class CompanyHQ(models.Model):
    company = models.ForeignKey(Company,  on_delete= models.CASCADE)
    hq_address = models.CharField(max_length=500)
    hq_city = models.CharField(max_length= 100)
    hq_country = models.CharField(max_length= 50)
    company_email = models.CharField(max_length=250)
    company_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return "HQ address" + self.hq_address

    class Meta:
        verbose_name_plural = 'Company HQ info'


class Message(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    customer_email = models.CharField(max_length= 100)
    customer_phone_number = models.CharField(max_length=100)
    customer_subject = models.CharField(max_length=200)
    customer_text = models.TextField(max_length=500)

