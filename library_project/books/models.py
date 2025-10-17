from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def clean(self):
        """
        Custom model-level validation:
        - Title and author must not be empty or whitespace.
        - Published date cannot be in the future.
        """
        if not self.title.strip():
            raise ValidationError({'title': 'Title cannot be empty.'})
        if not self.author.strip():
            raise ValidationError({'author': 'Author cannot be empty.'})
        if self.published_date and self.published_date > date.today():
            raise ValidationError({'published_date': 'Date cannot be in the future.'})

    def save(self, *args, **kwargs):
        """
        Overriding save to ensure clean() is always called before saving.
        """
        self.full_clean()  # Ensures all validations run
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.author})"
