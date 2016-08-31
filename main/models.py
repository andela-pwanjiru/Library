from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    """Model for book category"""
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey('Category')
    author = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.title
