from django.db import models
from django.urls import reverse

class Blog(models.Model):
    """
    Model representing a blog post.
    
    @param: None
    @desc: Define the fields for the Blog model, including title, author, and body.
    @returns: None
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )
    body = models.TextField()
    
    def __str__(self) -> str:
        """
        @param: None
        @desc: Return a string representation of the Blog instance, which is the title.
        @returns: A string representing the title of the blog post.
        """
        return self.title
    
    def get_absolute_url(self):
        """
        @param: None
        @desc: Get the absolute URL for the detail view of this blog post.
        @returns: A URL in the format "blog_detail/{pk}/" where {pk} is the primary key of the blog post.
        """
        return reverse("blog_detail", kwargs={"pk": self.pk})
