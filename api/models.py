from django.db import models

class DatabaseExplanation(models.Model):
    description = models.TextField()

class QueryCategory(models.Model):
    name = models.CharField(max_length=200)
    database_explanation = models.ForeignKey(DatabaseExplanation, on_delete=models.CASCADE)