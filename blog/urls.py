from django.urls import path, include
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'), 
    path('posts/new', views.PostCreateView.as_view(), name='post-create-page'),  
    path('posts', views.AllPostsView.as_view(), name='posts-page'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-detail-page'),
    path('posts/edit/<slug:slug>', views.PostUpdateView.as_view(), name='post-update-page'),
    path('posts/delete/<slug:slug>', views.PostDeleteView.as_view(), name='post-delete-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

