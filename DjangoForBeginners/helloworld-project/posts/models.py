from django.db import models

class Posts(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
