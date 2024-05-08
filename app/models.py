
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class BlogContent(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=200)
    paragraph = models.TextField()

    def __str__(self):
        return f"{self.blog_post.title} - {self.subtitle}"
class contact_detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name

