from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    prep = models.CharField(max_length=300, default="No Input")
    phone = models.IntegerField()
    desc = models.TextField()

class Update(models.Model):
    user_email = models.EmailField()