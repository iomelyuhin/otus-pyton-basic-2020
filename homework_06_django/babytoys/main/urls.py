from django.urls import path
from .views import MainListView

app_name = 'main'

urlpatterns = [
    path('', MainListView.as_view(), name='main'),
]
