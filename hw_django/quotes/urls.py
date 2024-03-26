from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path("", views.main, name='root'),
    path("<int:page>", views.main, name='root_paginate'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('show/', views.author_list, name='show'),
    path('all_quotes/', views.all_quotes, name='all_quotes'),
]
