from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    """
        post articles to main page
        TODO: add community auth?
    """
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)