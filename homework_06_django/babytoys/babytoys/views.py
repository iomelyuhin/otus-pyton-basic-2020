from django.views.generic.base import ContextMixin
from toys.models import Category, Card


class Menu(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(Menu, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class AllGoods(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(AllGoods, self).get_context_data()
        context['goods'] = Card.objects.all()
        return context


class AllCategories(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(AllCategories, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
