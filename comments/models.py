from django.contrib.auth import get_user_model
from django.db import models

from content.models import Titles

User = get_user_model()


class Reviews(models.Model):
    title = models.ForeignKey(Titles, on_delete=models.CASCADE, blank=True, null=True, related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    pub_date = models.DateTimeField('Дата публикации', auto_now=True)    


class Comments(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments") 
    pub_date = models.DateTimeField('дата публикации', auto_now=True)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE, related_name='comments')