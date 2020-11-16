from django.urls import path
from .views import MiniBooksListView, BigBooksCoversListView, \
    BigBooksPagesListView, BigBooksFullListView, \
    MiniBooksDetailView, BigBooksCoversDetailView, BigBooksFullDetailView, BigBooksPagesDetailView


app_name = 'toy'


urlpatterns = [
    path('mini/', MiniBooksListView.as_view(), name='mini-books'),
    path('big-covers/', BigBooksCoversListView.as_view(), name='big-books-covers'),
    path('big-pages/', BigBooksPagesListView.as_view(), name='big-books-pages'),
    path('big-full/', BigBooksFullListView.as_view(), name='big-books-full'),
    path('<int:pk>/', MiniBooksDetailView.as_view(), name="mini-detail"),
    path('<int:pk>/', BigBooksCoversDetailView.as_view(), name="big-covers-detail"),
    path('<int:pk>/', BigBooksFullDetailView.as_view(), name="big-full-detail"),
    path('<int:pk>/', BigBooksPagesDetailView.as_view(), name="big-pages-detail")
]
