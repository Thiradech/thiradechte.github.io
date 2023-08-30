from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path('new_page/', views.set_NewPage, name='new_page' ),
    path('create_newPage/', views.create_NewPage, name='create_newPage'),
    path('edit_page/<str:title>', views.edit_page, name='edit_page')
]
