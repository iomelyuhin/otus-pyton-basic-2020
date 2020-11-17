from django.urls import path
# from .views import MiniBooksListView, BigBooksCoversListView, \
#     BigBooksPagesListView, BigBooksFullListView, \
#     MiniBooksDetailView, BigBooksCoversDetailView, BigBooksFullDetailView, BigBooksPagesDetailView
from .views import CategoryDetailView, GoodDetailView


app_name = 'toys'


urlpatterns = [
    path('category-<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('item-<int:pk>/', GoodDetailView.as_view(), name='detail')
]
# urlpatterns = [
#     path('mini/', MiniBooksListView.as_view(), name='mini-books'),
#     path('big-covers/', BigBooksCoversListView.as_view(), name='big-books-covers'),
#     path('big-pages/', BigBooksPagesListView.as_view(), name='big-books-pages'),
#     path('big-full/', BigBooksFullListView.as_view(), name='big-books-full'),
#     path('good-<int:pk>/', MiniBooksDetailView.as_view(), name="good-detail"),
#     path('good-<int:pk>/', BigBooksCoversDetailView.as_view(), name="good-detail"),
#     path('good-<int:pk>/', BigBooksFullDetailView.as_view(), name="good-detail"),
#     path('good-<int:pk>/', BigBooksPagesDetailView.as_view(), name="good-detail")
# ]
