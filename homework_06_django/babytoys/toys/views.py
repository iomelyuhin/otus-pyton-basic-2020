from django.views.generic import DetailView
from .models import Card, Category
from babytoys.views import Menu, AllGoods, AllCategories


class CategoryDetailView(Menu, AllGoods, DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'list.html'


class GoodDetailView(Menu, DetailView):
    model = Card
    template_name = 'detail.html'
    context_object_name = 'good_item'
