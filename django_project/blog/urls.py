from django.urls import path
from .views import BlogListView, BlogDetailView


urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail") #new
]