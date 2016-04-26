#-*- coding: utf-8 -*-

from django.db import models


class Movie(models.Model):
	class Meta:
		db_table = "reviews"

	movie_title = models.CharField(max_length=180)
	movie_text = models.TextField()
	movie_date = models.DateTimeField('date published')
	movie_likes = models.IntegerField(default=0)


class Comments(models.Model):
	class Meta:
		db_table = "comments"

	comments_text = models.TextField(verbose_name='Текст комментария')
	comments_movie = models.ForeignKey(Movie)


# Create your models here.

	
	