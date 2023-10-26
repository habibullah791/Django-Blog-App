from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    """
    SignUpView allows new users to sign up for the website.

    @param: CreateView (Django generic view)
    @desc: This view extends Django's CreateView and is associated with the UserCreationForm, which is a built-in form for user registration. It provides a user registration form for new users to sign up and create an account. Upon successful registration, users are redirected to the login page.
    @returns: Rendered HTML page with a user registration form.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
