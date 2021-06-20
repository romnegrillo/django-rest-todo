from django.db import models

class Todo(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title