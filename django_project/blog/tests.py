from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Blog

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        """
        @param: None
        @desc: Set up data for testing by creating a user and a blog post.
        @returns: None
        """
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="1234"
        )
        cls.blog = Blog.objects.create(
            title="test",
            body="test body",
            author=cls.user
        )

    def test_post_model(self):
        """
        @param: None
        @desc: Test the Blog model's fields and methods.
        @returns: None
        """
        self.assertEqual(self.blog.title, "test")
        self.assertEqual(self.blog.body, "test body")
        self.assertEqual(self.blog.author.username, "testuser")
        self.assertEqual(str(self.blog.title), "test")
        self.assertEqual(self.blog.get_absolute_url(), "/blog/1/")

    def test_url_exist_at_correct_location_listview(self):
        """
        @param: None
        @desc: Test if the URL for the blog list view exists at the correct location.
        @returns: None
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exist_at_correct_location_detailview(self):
        """
        @param: None
        @desc: Test if the URL for the blog detail view exists at the correct location.
        @returns: None
        """
        response = self.client.get("/blog/1")
        self.assertEqual(response.status_code, 301)

    def test_blog_listview(self):
        """
        @param: None
        @desc: Test the behavior of the blog list view.
        @returns: None
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test body")
        self.assertTemplateUsed(response, "home.html")

    def test_blog_detailview(self):
        """
        @param: None
        @desc: Test the behavior of the blog detail view, including handling non-existing posts.
        @returns: None
        """
        response = self.client.get(reverse("blog_detail", kwargs={"pk": self.blog.pk}))
        no_response = self.client.get("/post/1122/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "test")
        self.assertTemplateUsed(response, "blog_detail.html")


    def test_post_createview(self):
        """
        @param: None
        @desc: Test the behavior of the blog post creation view.
        @returns: None
        """
        response = self.client.post(
            reverse("new_blog"),
            {
                "title" : "Title test",
                "body" : "Test body",
                "author" : self.user.username
            }
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Blog.objects.last().title, "test")
        self.assertEqual(Blog.objects.last().body, "test body")


    def test_blog_update(self):
        """
        @param: None
        @desc: Test the behavior of updating a blog post.
        @returns: None
        """
        response = self.client.post(
            reverse("edit_blog", args="1"),
            {
                "title" : "Updated title",
                "body" : "Updated Body"
            }
        )
        
        self.assertEqual(response.status_code, 302)