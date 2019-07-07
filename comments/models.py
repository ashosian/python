from django.db import models
from news.models import News
from django.contrib.auth.models import User 

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=500)
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True)
    written_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"

