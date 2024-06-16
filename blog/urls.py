from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path("post/<int:id>/", views.post, name='post'),
    path("", views.blog, name='blog'),
    path("exemplo/", views.exemplo, name='exemplo')
]