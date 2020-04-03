from django.contrib import admin
from django.urls import path, include
from p_library import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('book_list/', views.books_list),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publishers/', views.publishers),
    path('p_library/', include('p_library.urls', namespace='p_library')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)