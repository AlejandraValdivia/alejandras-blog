from django.urls import path, include
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'), #probably will delete this
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail-page'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

