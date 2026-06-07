from django.db import models

class Result(models.Model):
    score = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f"{self.score}/{self.total}"
