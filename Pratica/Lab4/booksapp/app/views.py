from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Publisher

# Create your views here.
def booksearch(request):
    if 'query' in request.POST:
        query = request.POST['query']

        if query:
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html', {'books': books, 'query': query})
        else:
            return render(request, 'booksearch.html', {'error': True})
    else:
        return render(request, 'booksearch.html', {'error': False})
    
def authorsearch(request):
    if 'query' in request.POST:
        query = request.POST['query']

        if query:
            authors = Author.objects.filter(name__icontains=query)
            return render(request, 'authorslist.html', {'authors':authors, 'query': query})
        else:
            return render(request, 'authorsearch.html', {'error': True})
    else:
        return render(request, 'booksearch.html', {'error': False})
    
def publishersearch(request):
    if 'query' in request.POST:
        query = request.POST['query']

        if query:
            publishers = Publisher.objects.filter(name__icontains=query)
            return render(request, 'publisherslist.html', {'publishers': publishers, 'query': query})
        else:
            return render(request, 'publishersearch.html', {'error':True})
    else:
        return render(request, 'publishersearch.html', {'error': False})


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

def getPublisherBooks(request,publisher):
    books = Book.objects.filter(publisher__name=publisher)
    context = {
        'publisher': publisher,
        'books': books
    }
    return render(request, 'publisherbooks.html', context)


def publisherAuthors(request, publisher_name):
    publisher = Publisher.objects.get(name=publisher_name)
    authors = Author.objects.filter(book__publisher=publisher)
    context = {
        "publisher": publisher,
        "authors": authors,
    }
    return render(request, 'publisherauthors.html', context)


def insertAuthors(request):
    if 'name' in request.POST and 'email' in request.POST:
        name = request.POST['name']
        email = request.POST['email']

        if name and email:
            a = Author(name=name, email=email)
            a.save()

            authors = Author.objects.all()
    
            return render(request, 'authorslist.html', {'authors': authors})
        else:
            return render(request, 'authorinsert.html', {'error': True })
    else:
        return render(request, 'authorinsert.html', {'error': False})
    

def insertPublisher(request):
    if 'name' in request.POST and 'city' in request.POST and 'country' in request.POST and 'website' in request.POST:
        name = request.POST['name']
        city = request.POST['city']
        country = request.POST['country']
        website = request.POST['website']

        if name and city and country and website:
            p = Publisher(name=name, city=city, country=country, website=website)
            p.save()

            publishers = Publisher.objects.all()

            return render(request, 'publisherslist.html', {'publishers': publishers})
        else:
            return render(request, 'publisherinsert.html', {'error': True})
        
    else:
        return render(request, 'publisherinsert.html', {'error': False})

