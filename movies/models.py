from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=100,null=False)
    img = models.ImageField(null=False,upload_to='static/movies/')
    description = models.TextField(null=True)
    rating = models.DecimalField(max_digits=4,decimal_places=2)

class Reviews(models.Model):
    reviewer = models.CharField(max_length=100,null=False)
    movie_title = models.CharField(max_length=100,null=False)
    review = models.TextField(null=False)
    review_type = models.BooleanField(default=False)
   
