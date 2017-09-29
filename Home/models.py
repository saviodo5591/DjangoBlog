from django.db import models


class Post(models.Model):
    postTitle = models.CharField(max_length=140)
    postBody = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
