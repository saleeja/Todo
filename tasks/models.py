from django.db import models


class Task(models.Model):
    title=models.CharField(max_length=150)
    datetime=models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)
    is_deleted=models.BooleanField(default=False)

    def __str__(self):
        return self.title


