from django.urls import path
from .views import MiniBooksListView, BigBooksCoversListView, BigBooksPagesListView, BigBooksFullListView


app_name = 'toy'


urlpatterns = [
    # path('', include())
    path('mini/', MiniBooksListView.as_view(), name='MiniBooks'),
    path('big-covers/', BigBooksCoversListView.as_view(), name='BigBooksCovers'),
    path('big-pages/', BigBooksPagesListView.as_view(), name='BigBooksPages'),
    path('big-full/', BigBooksFullListView.as_view(), name='BigBooksFull'),
]
