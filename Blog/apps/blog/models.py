from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Add in Blog model a boolean field enabled to make some posts published or unpublished
    enabled = models.BooleanField(default=True)

class Comment(models.Model):
    # Create a new model Comments with text and blog foreign key, here we will save comments for each blog post
    text = models.TextField(default="test")
    blog = models.ForeignKey('Blog', related_name='comments', on_delete=models.CASCADE)