from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100) 
    body = models.TextField(default='')
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(default='fallback.png', blank=True)
    
    def __str__(self):
        return self.title