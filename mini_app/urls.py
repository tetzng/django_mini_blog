from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("new/",views.new,name="new"),
    path("article/all/", views.article_all, name="article_all"),
    path("article/<int:pk>/", views.view_article,name="view_article"),
    path("article/<int:pk>/edit/", views.edit,name="edit"),
    path("article/<int:pk>/update/",views.update_post,name="update_post"),
    path("article/<int:pk>/delete/", views.delete,name="delete"),
    path("article/<int:pk>/like/", views.like,name="like"),
    path("api/like/<int:pk>/", views.api_like, name="api_like"),
    path("post/",views.add,name="add"),
    path("tag/<int:pk>/", views.view_tag, name="view_tag"),
]