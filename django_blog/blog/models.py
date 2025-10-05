# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    """
    Comment on a Post.
    - post: the post this comment belongs to
    - author: user who created the comment
    - content: comment text
    - created_at / updated_at: timestamps
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]  # oldest first

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    def get_update_url(self):
        return reverse("comment_edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("comment_delete", kwargs={"pk": self.pk})
