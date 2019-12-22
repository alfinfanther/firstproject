from django.db import models
from utils.models import CreateUpdate


# Create your models here.
class Province(CreateUpdate):
    code = models.IntegerField()
    name = models.CharField(max_length=255, blank=True)
 
    def __str__(self):
        return self.name
 
class City(CreateUpdate):
    code = models.IntegerField()
    name = models.CharField(max_length=255, blank=True)
    province = models.ForeignKey(Province, related_name='city',on_delete=models.PROTECT)
 
    def __str__(self):
        return self.name

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication, related_name='publication')

    class Meta:
        ordering = ('headline',)

    def __str__(self):
        return self.headline