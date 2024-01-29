from django.shortcuts import render
from .models import Author, Book, Publisher

# Create your views here.
def listbooks(request):
    books = Book.objects.all()
    bparams = {
        "books" : books
    }
    return render(request, 'booklist.html', bparams)

def bookdetails(request, title):
    bookDet = Book.objects.get(title=title)
    bdparams = { 
        'book': bookDet
    }
    return render(request, 'bookdetails.html', bdparams)

def listauthors(request):
    authors = Author.objects.all()
    aparams = {
        "authors": authors
    }
    return render(request, 'authorslist.html', aparams)

def authordetails(request, name):
    authorDet = Author.objects.get(name=name)
    adparams = {
        "author": authorDet
    }
    return render(request, 'authordetails.html',adparams)

def listpublisher(request):
    publishers = Publisher.objects.all()
    pparams = {
        "publishers": publishers
    }
    return render(request, 'publisherslist.html', pparams)

def publisherdetails(request, name):
    publisherDet = Publisher.objects.get(name=name)
    pdparams = {
        "publisher": publisherDet
    }
    return render(request, 'publisherdetails.html',pdparams)

def getAuthorBooks(request,author):
    books = Book.objects.filter(authors__name=author)
    context = {
        "author": author,
        "books": books
    }
    return render(request, 'authorbooks.html', context)

def publisherAuthors(request, publisher_name):
    publisher = Publisher.objects.get(name=publisher_name)
    authors = Author.objects.filter(book__publisher=publisher)
    context = {
        "publisher": publisher,
        "authors": authors,
    }
    return render(request, 'publisherauthors.html', context)
