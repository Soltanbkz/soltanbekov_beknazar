from django.db import models

class Price(models.Model):
    mark = models.CharField('Mark', default="ВЫГОДНО", max_length=30)
    photo = models.FileField(upload_to='photos/')
    service = models.CharField('Service', max_length=100)
    name = models.CharField('Title', max_length=50)
    text = models.TextField('Text')
    old_price = models.IntegerField('Old Price')
    new_price = models.IntegerField('New Price')