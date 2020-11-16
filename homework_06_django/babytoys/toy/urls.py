from django.urls import path
from .views import MiniBooksListView, BigBooksCoversListView, BigBooksPagesListView, BigBooksFullListView


app_name = 'toy'


urlpatterns = [
    # path('', include())
    path('mini/', MiniBooksListView.as_view(), name='mini-books'),
    path('big-covers/', BigBooksCoversListView.as_view(), name='big-books-covers'),
    path('big-pages/', BigBooksPagesListView.as_view(), name='big-books-pages'),
    path('big-full/', BigBooksFullListView.as_view(), name='big-book-full'),
]
