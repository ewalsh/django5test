from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Review
from .utils import average_rating

# Create your views here.
# def index(request):
#     name = request.GET.get('name') or 'world'
#     # return HttpResponse('Hello {}'.format(name))
#     return(
#         render(request, 'base.html', {'name': name})
#     )

# functional view 
def welcome_view(request):
    bk_cnt = Book.objects.using('reviews').count()
    scnd = 'come'
    # message = "<html><h1>Welcome to Bookr!</h1> "\
    # "<p>{} books and counting! More to {}</p></html>".format(bk_cnt, scnd)
    # return HttpResponse(message)
    return(
        render(request, 'base.html')
    )


def book_list(request):
    books = Book.objects.using('reviews').all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for \
                                          review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,\
                          'book_rating': book_rating,\
                          'number_of_reviews': number_of_reviews})
        context = {
            'book_list': book_list
        }
        return render(request, 'reviews/book_list.html', context)

