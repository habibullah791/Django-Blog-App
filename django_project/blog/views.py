from django.views.generic import ListView, DetailView
from .models import Blog

class BlogListView(ListView):
    """
    BlogListView displays a list of blog posts.

    @param: ListView (Django generic view)
    @desc: This view extends Django's ListView and is associated with the Blog model. It retrieves all blog posts and renders them in the "home.html" template.
    @returns: Rendered HTML page with a list of blog posts.
    """
    model = Blog
    template_name = "home.html"

class BlogDetailView(DetailView):
    """
    BlogDetailView displays the details of a single blog post.

    @param: DetailView (Django generic view)
    @desc: This view extends Django's DetailView and is associated with the Blog model. It retrieves a specific blog post based on its primary key and renders the details in the "blog_detail.html" template.
    @returns: Rendered HTML page with the details of a single blog post.
    """
    model = Blog
    template_name = "blog_detail.html"
