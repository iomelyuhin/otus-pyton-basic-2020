from django.shortcuts import render
from django.views.generic import ListView, DetailView
from babytoys.views import Menu
from toys.models import Card


class MainListView(Menu, ListView):
    model = Card
    template_name = 'main/index.html'


# def main_view(request):
#     return render(request, 'main/index.html')
