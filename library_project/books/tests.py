from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Book
from datetime import date, timedelta

class BookModelTests(TestCase):
    """
    Unit tests for Book model validation and CRUD operations.
    """

    def test_title_cannot_be_empty(self):
        """
        The model should raise ValidationError if title is empty.
        """
        book = Book(title='', author='Author', published_date=date.today())
        with self.assertRaises(ValidationError):
            book.full_clean()

    def test_future_date_not_allowed(self):
        """
        The model should raise ValidationError if published_date is in the future.
        """
        future = date.today() + timedelta(days=10)
        book = Book(title='Future Book', author='Time Lord', published_date=future)
        with self.assertRaises(ValidationError):
            book.full_clean()

    def test_valid_book_saves(self):
        """
        Valid book should be saved successfully to the database.
        """
        book = Book(title='Valid Book', author='Author', published_date=date.today())
        book.full_clean()  # Should not raise any error
        book.save()
        self.assertEqual(Book.objects.count(), 1)

