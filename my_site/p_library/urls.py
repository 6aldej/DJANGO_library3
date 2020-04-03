from django.urls import path  
from .views import AuthorEdit, AuthorList, book_author_create_many

app_name = 'p_library'

urlpatterns = [  
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='authors_list'),
    path('author_book/create_many', book_author_create_many, name='author_book_create_many'),
]