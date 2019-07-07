from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    CATEGORY = (("0", "Politics"), ("1", "Sports"), ("2", "International"))
    title = models.CharField(max_length=250)
    content = models.TextField(verbose_name="article")
    category = models.CharField(choices=CATEGORY, max_length=2)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    count = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to='uploads')

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    


