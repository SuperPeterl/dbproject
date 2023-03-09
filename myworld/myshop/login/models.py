from django.db import models

# Create your models here.
class employee(models.Model):
    emp_user = models.CharField( max_length=20)
    emp_pass = models.CharField( max_length=20)
    emp_fname = models.CharField( max_length=20)
    emp_lname = models.CharField( max_length=20)
    emp_sex = models.CharField( max_length=1)