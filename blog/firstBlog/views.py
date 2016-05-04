from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from firstBlog.models import Movie, Comments
from django.core.exceptions import ObjectDoesNotExist
from firstBlog.forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
# Create your views here.



def basic_one(request):
	view = 'basic_one'
	html = '<html><body><h1 align="center">This is %s view</h1></body></html>' %view
	return HttpResponse(html)


def template_2(request):
	view = 'template_2'	
	template = get_template('view.html')
	html = template.render(Context({'name': view}))
	return HttpResponse(html)


def template_3(request):
	view = 'template_3'
	return render_to_response('view.html', {'name': view})


def movies(request, page_number=1):
	all_movies = Movie.objects.all()
	active_page = Paginator(all_movies, 4)
	return render_to_response('movies.html', {'movies': active_page.page(page_number), 'username': auth.get_user(request).username})


def movie(request, movie_id=1):
	comment_form = CommentForm
	args = {}
	args.update(csrf(request))
	args['movie'] = Movie.objects.get(id=movie_id)
	args['comments'] = Comments.objects.filter(comments_movie_id=movie_id)
	args['form'] = comment_form
	args['username'] = auth.get_user(request).username
	return render_to_response('movie.html', args)



def addlike(request, movie_id):
	try:
		if movie_id in request.COOKIES:
			redirect('/')
		else:	
			movie = Movie.objects.get(id=movie_id)
			movie.movie_likes += 1
			movie.save()
			response = redirect('/')
			response.set_cookie(movie_id, 'test')
		   	return response
	except ObjectDoesNotExist:
		raise Http404
	return redirect('/')	


def addcomment(request, movie_id):
	if request.POST and ('pause' not in request.session):
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.comments_movie = Movie.objects.get(id=movie_id)
			form.save()
			request.session.set_expiry(60)
			request.session['pause'] = True 
	return redirect('/movies/get/%s/' % movie_id)		
					

