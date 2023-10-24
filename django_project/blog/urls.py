from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"), #new
    path("blog/new/", BlogCreateView.as_view(), name="new_blog"), #new
    path("blog/<int:pk>/edit", BlogUpdateView.as_view(), name="edit_blog"), #new
    path("blog/<int:pk>/del", BlogDeleteView.as_view(), name="del_blog"), #new
]