import graphene
from graphene_django import DjangoObjectType
from .models import Book

#This process is kind of a serialization
class BooksType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'excerpt')

class Query(graphene.objectType):
    all_books = graphene.List(BooksType)

schema = graphene.Schema(query=Query)
