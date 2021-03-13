from django.urls import path
from . import views
from .feeds import LatestPostFeed

app_name = 'blog'

urlpatterns = [
    path('', views.post_lists, name='post_list'),
    path('tag/<slug:tag_slug>', views.post_lists, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_details,
         name='post_details'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search')
]


