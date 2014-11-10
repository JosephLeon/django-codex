from django.db import models


class Resource(models.Model):
    resource_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    resource_link = models.URLField()
    resource_review = models.TextField()


class UserReview(models.Model):
    resource = models.ForeignKey(Resource)
    user_review = models.TextField()
    votes = models.IntegerField(default=0)
