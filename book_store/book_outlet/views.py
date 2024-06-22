from django.shortcuts import render

from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.

def index(request):
    books=Book.objects.all().order_by("-title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating")) 
    return render(request, "book_outlet/index.html", 
                  {"books_list":books, 
                   "total_number_of_books":num_books,
                   "average_rating":avg_rating["rating__avg"]})


def book_detail(request, id):
    try:
        book=Book.objects.get(pk=id)
    except:
        raise Http404("This Book Doesnot Exists !")
    return render(request, "book_outlet/book_detail.html",
                  {"title": book.title,
                   "aurthor": book.aurthor,
                   "rating": book.rating,
                   "is_bestseller": book.is_bestselling})