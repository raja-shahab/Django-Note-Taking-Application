from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']