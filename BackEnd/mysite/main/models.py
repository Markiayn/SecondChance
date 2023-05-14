from django.db import models

# Create your models here.
class Article(models.Model):

    
    title = models.CharField(max_length=50)
    fulltext = models.TextField()
    summary = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    pubdate = models.DateTimeField()
    # isPublished = models.BooleanField()  #TODO

