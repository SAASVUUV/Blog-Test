from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from datetime import date
# Create your models here.





    
class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"




class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"







class Post(models.Model):
    title = models.CharField(max_length= 80)
    excerpt = models.CharField(max_length= 250)
    image = models.ImageField(upload_to="posts", null=True)
    content = models.TextField()
    slug = models.SlugField(unique=True, db_index=True)
    date = models.DateField((""), auto_now=False, auto_now_add=False, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)


    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])

    def __str__(self):
        return f"{self.title}"
    

class Comment(models.Model):
    user_name = models.CharField(max_length=25)
    comment_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True)