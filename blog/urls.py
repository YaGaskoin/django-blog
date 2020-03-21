from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import PostSitemap


app_name = "blog"

sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name="post_list"),
    #path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail,  name='post_detail'),
    path("<int:post_id>/share/", views.post_share, name="post_share")
]
