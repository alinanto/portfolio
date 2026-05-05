from django.db import models
from django.utils.text import slugify
from martor.models import MartorField

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
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    short_description = models.TextField(max_length=500)

    markdown_content = MartorField()

    github_link = models.URLField(blank=True)

    tags = models.CharField(
        max_length=300,
        help_text="Comma separated tags like python,django,cpp"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

    def __str__(self):
        return self.title