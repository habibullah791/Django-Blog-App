from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


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
    

class BlogDetailView(DetailView):
    """
    BlogDetailView displays the details of a single blog post.

    @param: DetailView (Django generic view)
    @desc: This view extends Django's DetailView and is associated with the Blog model. It retrieves a specific blog post based on its primary key and renders the details in the "blog_detail.html" template.
    @returns: Rendered HTML page with the details of a single blog post.
    """
    model = Blog
    template_name = "blog_detail.html"

class BlogCreateView(CreateView):
    """
    BlogCreateView allows users to create a new blog post.

    @param: CreateView (Django generic view)
    @desc: This view extends Django's CreateView and is associated with the Blog model. It provides a form for users to create a new blog post and uses the "new_blog.html" template.
    @returns: Rendered HTML page with a form to create a new blog post.
    """
    model = Blog
    template_name = "new_blog.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    """
    BlogUpdateView allows users to update an existing blog post.

    @param: UpdateView (Django generic view)
    @desc: This view extends Django's UpdateView and is associated with the Blog model. It allows users to edit and update an existing blog post's title and body using the "edit_blog.html" template.
    @returns: Rendered HTML page with a form to edit and update a blog post.
    """
    model = Blog
    template_name = "edit_blog.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    """
    BlogDeleteView allows users to delete an existing blog post.

    @param: DeleteView (Django generic view)
    @desc: This view extends Django's DeleteView and is associated with the Blog model. It enables users to delete an existing blog post, and upon successful deletion, redirects to the "home" view.
    @returns: Deletion of a blog post and redirection to the home page.
    """
    model = Blog
    template_name = "del_blog.html"
    success_url = reverse_lazy("home")
