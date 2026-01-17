from django.shortcuts import render

# Create your views here.

# bookdetails/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Comment

# Home page shows latest books
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# List page (CRUD)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Book detail page with comments
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        content = request.POST.get('content')
        if name and content:
            Comment.objects.create(book=book, name=name, content=content)
            return redirect('book_detail', id=id)
    return render(request, 'book_detail.html', {'book': book})

# Create book
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        Book.objects.create(title=title, author=author, description=description, image=image)
        return redirect('book_list')
    return render(request, 'book_create.html', {'book': None})  # pass None for create
# Update book

def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.title = request.POST.get('title', book.title)
        book.author = request.POST.get('author', book.author)
        book.description = request.POST.get('description', book.description)
        if request.FILES.get('image'):
            book.image = request.FILES.get('image')
        book.save()
        return redirect('book_list')
    return render(request, 'book_create.html', {'book': book})  # pass book for update



# Delete book
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')