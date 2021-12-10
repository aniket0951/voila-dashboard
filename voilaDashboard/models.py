from django.db import models

# Create your models here.

class voila_sub_user(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    auth_token = models.CharField(max_length=255, null=True, blank=True)
    auth_token = models.CharField(max_length=255, null=True, blank=True)
    staus = models.CharField(max_length=255, null=True, blank=True)
    employee_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "voila_sub_user"