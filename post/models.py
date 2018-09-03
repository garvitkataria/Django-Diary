# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Post (models.Model):
	title=models.CharField(max_length=140)
	body=models.TextField()
	date=models.DateTimeField(default=datetime.now(),blank=True)

	def __str__(self):
		return self.title
	def goto(self):
		return reverse('post:index')
