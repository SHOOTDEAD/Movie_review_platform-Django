from django.db import models



class Reviewers(models.Model):
    name = models.CharField(unique=True, max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
