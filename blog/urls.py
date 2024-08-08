from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail-page'),
]


