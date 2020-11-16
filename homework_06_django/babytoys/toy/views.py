from django.shortcuts import render
from django.views.generic import ListView
from .models import Card, Images


class MiniBooksListView(ListView):
    model = Card
    context_object_name = 'goods_list'
    template_name = 'list.html'
    queryset = Card.objects.filter(category_id=2).all()


class BigBooksCoversListView(ListView):
    model = Card
    context_object_name = 'goods_list'
    template_name = 'list.html'
    queryset = Card.objects.filter(element_id=1).all()


class BigBooksPagesListView(ListView):
    model = Card
    context_object_name = 'goods_list'
    template_name = 'list.html'
    queryset = Card.objects.filter(element_id=2).all()


class BigBooksFullListView(ListView):
    model = Card
    context_object_name = 'goods_list'
    template_name = 'list.html'
    queryset = Card.objects.filter(element_id=3).all()


# class ImagesListView(ListView):
#     model = Images
#     context_object_name = 'goods_images_list'
#     template_name = 'list.html'

# Create your views here.
