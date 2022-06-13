from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    createdDate = models.DateTimeField(editable=False)
    publishedDate = models.DateTimeField(editable=False)

    def __str__(self) -> str:
        return self.title
