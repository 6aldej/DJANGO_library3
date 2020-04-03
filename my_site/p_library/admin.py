from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    
    list_display=('title','author_full_name', 'full_count', 'image')
    list_filter = ('author', 'full_count', 'friends')

    fields=('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'publisher', 'friends', 'full_count', 'image')
    filter_horizontal = ('friends',)

    
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass