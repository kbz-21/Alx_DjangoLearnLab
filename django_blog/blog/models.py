from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    """
    Blog Post model.
    - title: short title
    - content: body
    - published_date: auto-set when created
    - author: User foreign key, one user -> many posts
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # used by CreateView/UpdateView to redirect to detail page
        return reverse("post_detail", kwargs={"pk": self.pk})
