from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import BookForm

def book_list(request):
    """
    Display a list of all books.
    """
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_create(request):
    """
    Handle book creation.
    Uses try/except to handle errors gracefully and
    provides feedback messages to the user.
    """
    form = BookForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Book added successfully.')
                return redirect('book_list')
            else:
                messages.warning(request, 'Please correct the form errors.')
        except Exception as e:
            messages.error(request, f'Error saving book: {e}')
    return render(request, 'books/book_form.html', {'form': form})


def book_update(request, pk):
    """
    Handle book update.
    Uses get_object_or_404 for safe object retrieval and try/except for error handling.
    """
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Book updated successfully.')
                return redirect('book_list')
            else:
                messages.warning(request, 'Please check the form for errors.')
        except Exception as e:
            messages.error(request, f'Error updating book: {e}')
    return render(request, 'books/book_form.html', {'form': form})


def book_delete(request, pk):
    """
    Handle book deletion with confirmation.
    """
    try:
        book = get_object_or_404(Book, pk=pk)
        if request.method == 'POST':
            book.delete()
            messages.success(request, 'Book deleted successfully.')
            return redirect('book_list')
    except Exception as e:
        messages.error(request, f'Error deleting book: {e}')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
