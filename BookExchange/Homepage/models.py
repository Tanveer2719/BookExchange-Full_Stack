from django.db import models
"""
what is models ?
    It is basically the blueprint of the database
    It helps to know how you are going to store data for this app
"""
# Create your models here.

class Author(models.Model):
    authorName = models.CharField(max_length=255)
    profileUrl = models.CharField(max_length=500)

    def __str__(self):
        return self.authorName

class Book(models.Model):
    title = models.CharField(max_length=255)
    edition = models.IntegerField()
    publisher = models.CharField(max_length=255) 
    imageUrl = models.CharField(max_length=500)
    dateAdded = models.DateTimeField(auto_now_add= True)
    purpose = models.CharField(max_length=15)
    description = models.CharField(max_length=500)
    authorsOfBook = models.ManyToManyField(Author)

    def __str__(self):
        return self.title + " " + self.publisher