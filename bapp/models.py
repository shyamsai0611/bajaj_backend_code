from django.db import models

class Details(models.Model):
    Status = models.BooleanField()
    User_id = models.CharField(max_length=255)
    Email_id = models.EmailField()
    roll = models.CharField(max_length=255)
    numbers = models.JSONField(default=list, blank=True)
    alphabets = models.JSONField(default=list, blank=True)
    highest_alphabet = models.JSONField(default=list, blank=True)