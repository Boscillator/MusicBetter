from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/<str:song>', views.results, name='results'),
    path('search', views.search_by_name, name='search')
]  