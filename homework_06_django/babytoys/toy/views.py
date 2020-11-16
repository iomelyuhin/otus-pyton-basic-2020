from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Card, Images


class MiniBooksListView(ListView):
    model = Card
    context_object_name = 'goods_list'
    template_name = 'list.html'
    queryset = Card.objects.filter(category_id=2).all()


class MiniBooksDetailView(DetailView):
    model = Card
    template_name = 'detail.html'
    context_object_name = 'good_item'


class BigBooksCoversListView(ListView):
    model = Card
    context_object_name = 'goods_list'
    template_name = 'list.html'
    queryset = Card.objects.filter(element_id=1).all()


class BigBooksCoversDetailView(DetailView):
    model = Card
    template_name = 'detail.html'
    context_object_name = 'good_item'


class BigBooksPagesListView(ListView):
    model = Card
    context_object_name = 'goods_list'
    template_name = 'list.html'
    queryset = Card.objects.filter(element_id=2).all()


class BigBooksPagesDetailView(DetailView):
    model = Card
    template_name = 'detail.html'
    context_object_name = 'good_item'


class BigBooksFullListView(ListView):
    model = Card
    context_object_name = 'goods_list'
    template_name = 'list.html'
    queryset = Card.objects.filter(element_id=3).all()


class BigBooksFullDetailView(DetailView):
    model = Card
    template_name = 'detail.html'
    context_object_name = 'good_item'
