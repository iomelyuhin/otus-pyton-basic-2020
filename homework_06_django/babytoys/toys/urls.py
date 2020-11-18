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
