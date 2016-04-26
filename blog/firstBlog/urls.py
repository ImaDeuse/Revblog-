from django.conf.urls import include, url




urlpatterns = [
    
    url(r'^1/', 'firstBlog.views.basic_one'),
    url(r'^2/', 'firstBlog.views.template_2'),
    url(r'^3/', 'firstBlog.views.template_3'),
    url(r'^movies/all/$', 'firstBlog.views.movies'),
    url(r'^movies/get/(?P<movie_id>\d+)/$', 'firstBlog.views.movie'),
    url(r'^movies/addlike/(?P<movie_id>\d+)/$', 'firstBlog.views.addlike'),
    url(r'^movies/addcomment/(?P<movie_id>\d+)/$', 'firstBlog.views.addcomment'),
    url(r'^', 'firstBlog.views.movies'),

]
