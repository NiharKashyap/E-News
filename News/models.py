from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class News(models.Model):
    title = models.TextField()
    body = models.TextField()
    posted = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-posted']

    def __str__(self):
        return str(self.id)

class BookMarks(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    news = models.ForeignKey(News ,on_delete=CASCADE)
    
    class Meta:
        verbose_name_plural = 'BookMarks'

    def __str__(self):
        #return "Bookmark" + str(self.id)
        return str(self.id)