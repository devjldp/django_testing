from django import forms
from .models import Book
from datetime import date

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    def clean_title(self):
        """
        Extra form-level validation.
        Ensures title has at least 2 characters.
        """
        title = self.cleaned_data['title']
        if len(title) < 2:
            raise forms.ValidationError("Title must have at least 2 characters.")
        return title
