from django.conf.urls import url
from django.views.generic import ListView
from . import views, models


urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^new-post/', views.new_post),
    url(r'^posts/$', ListView.as_view(queryset=models.Post.objects.all().order_by("-date")[:15],
                                         template_name="posts.html")),
]