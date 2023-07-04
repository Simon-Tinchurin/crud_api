from django.db import models


# Task model
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
