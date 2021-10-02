from django.shortcuts import render

# Create your views here.
class Article(models.Model):
    title = models.CharField()
    content = models.TextField()