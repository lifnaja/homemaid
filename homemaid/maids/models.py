from django.db import models


class Maid(models.Model):
    name = models.CharField(max_length=255)
    profile_image = models.FileField()
    birthday = models.DateField()
    description = models.TextField()
    certificate = models.TextField()
    salary = models.IntegerField()
