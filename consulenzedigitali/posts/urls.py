from django.conf.urls import url, include
from django.contrib import admin
from . import views as posts_views
from django.views.generic import ListView, DetailView
from .models import Post
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    url(r'^$',posts_views.homepage, name="home"),
    url(r'^chisono/$',posts_views.chisono, name="chisono"),
    url(r'^servizi/$',posts_views.servizi, name="servizi"),
    url(r'^contatto/$',posts_views.contatto, name="contatto"),

    url(r'^lista-post/$', ListView.as_view(
        queryset = Post.objects.all().order_by("-date"),
        template_name = "lista_post.html"
    ), name = "lista"),

    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model = Post,
        template_name = "post_singolo.html"
    ), name = "lista"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)