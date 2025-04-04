from django.db import models

class Victim(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


from django.db import models

class Victim(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=9, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    id_number = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    motivational_letter = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

