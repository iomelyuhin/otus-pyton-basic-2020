from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Card, Images, Category
from babytoys.views import Menu, AllGoods, AllCategories


class CategoryDetailView(Menu, AllGoods, DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'list.html'


class GoodDetailView(Menu, AllCategories, DetailView):
    model = Card
    template_name = 'detail.html'
    context_object_name = 'good_item'




# class MiniBooksListView(Menu, ListView):
#     model = Card.mini_books()
#     context_object_name = 'goods_list'
#     template_name = 'list.html'
#     queryset = Card.objects.filter(category_id=2).all()
#
#
# class MiniBooksDetailView(Menu, ParentDirectory, DetailView):
#     model = Card
#     template_name = 'detail.html'
#     context_object_name = 'good_item'
#     parent_dir = "/toys/mini/"
#
#
# class BigBooksListView(Menu, ListView):
#     model = Card
#     context_object_name = 'goods_list'
#     template_name = 'list.html'
#     queryset = Card.objects.filter(category_id=1).all()
#
#
# class BigBooksCoversListView(Menu, ListView):
#     model = Card
#     context_object_name = 'goods_list'
#     template_name = 'list.html'
#     queryset = Card.objects.filter(element_id=1).all()
#
#
# class BigBooksCoversDetailView(Menu, ParentDirectory, DetailView):
#     model = Card
#     template_name = 'detail.html'
#     context_object_name = 'good_item'
#     parent_dir = "/toys/big-covers/"
#
#
# class BigBooksPagesListView(Menu, ListView):
#     model = Card
#     context_object_name = 'goods_list'
#     template_name = 'list.html'
#     queryset = Card.objects.filter(element_id=2).all()
#
#
# class BigBooksPagesDetailView(Menu, ParentDirectory, DetailView):
#     model = Card
#     template_name = 'detail.html'
#     context_object_name = 'good_item'
#     parent_dir = "/toys/big-pages/"
#
#
# class BigBooksFullListView(Menu, ListView):
#     model = Card
#     context_object_name = 'goods_list'
#     template_name = 'list.html'
#     queryset = Card.objects.filter(element_id=3).all()
#
#
# class BigBooksFullDetailView(Menu, ParentDirectory, DetailView):
#     model = Card
#     template_name = 'detail.html'
#     context_object_name = 'good_item'
#     parent_dir = "/toys/big-full/"
