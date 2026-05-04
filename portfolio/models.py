from django.db import models

class Visit(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    first_visit = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"