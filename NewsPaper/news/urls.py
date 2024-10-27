from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [path('post/', PostList.as_view()),
               path('news/', PostDetail.as_view(), name='post_detail'),
               ]