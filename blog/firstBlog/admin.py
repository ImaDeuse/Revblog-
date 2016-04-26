from django.contrib import admin
from firstBlog.models import Movie,Comments

class MovieInline(admin.StackedInline):
	model = Comments
	extra = 1
	

class MovieAdmin(admin.ModelAdmin):
	fields = ['movie_title', 'movie_text', 'movie_date']
	inlines = [MovieInline]
	list_filter = ['movie_date']


admin.site.register(Movie, MovieAdmin)


# Register your models here.
