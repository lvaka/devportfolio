# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Site(models.Model):

	name = models.CharField(max_length=20)
	image = models.ImageField(upload_to='uploads/')
	url = models.URLField(max_length=100)
	description = models.TextField()
	technology = models.TextField()

	def __str__(self):
		return self.name

class PortfolioImage(models.Model):

	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='portfolio/')

	def __str__(self):
		return self.name