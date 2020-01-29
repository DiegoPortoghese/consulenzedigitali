from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="posts/img/%Y/%m/%d")
    title = models.CharField(max_length=500)
    content = models.TextField(blank = True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

