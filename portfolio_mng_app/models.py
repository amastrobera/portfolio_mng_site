from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

fullDateFormat = "%a, %d-%b-%Y - %H:%M:%S"
miniDateFormat = "%d-%b-%Y"

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return '{}, e-mail: {}'.format(self.name, self.email)

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now(),editable=False)
    last_update_date = models.DateTimeField(default=timezone.now())
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def creationDate(self):
        return self.creation_date.strftime(fullDateFormat)
    def creationDateMini(self):
        return self.creation_date.strftime(miniDateFormat)
    def lastUpdateDate(self):
        return self.last_update_date.strftime(fullDateFormat)
    def lastUpdateDateMini(self):
        return self.last_update_date.strftime(miniDateFormat)
        
    def __str__(self):
        return '{}, created on {}, last updated on {}'.format(self.name,
                self.creation_date.strftime(fullDateFormat),
                self.last_update_date.strftime(fullDateFormat))
    def save(self, *args, **kwargs):
        self.last_update_date = timezone.now()
        return super(Portfolio, self).save(*args, **kwargs)


class Asset(models.Model):
    yid = models.CharField(max_length=10)
    position = models.IntegerField(default=0)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
        
    def __str__(self):
        return '{}: {}'.format(self.yid, self.position)


class Security(models.Model):
    yid = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return '{}: {}'.format(self.yid, self.name)

