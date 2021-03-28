from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/<str:song>', views.results, name='results'),
]  