from django.urls import path
from .views import *
app_name = 'home'


urlpatterns = [
    path('', page_home, name='page_home'),
    # path('comment/',  CommentListView.as_view(), name='comment'),
    # path('comment/<int:pk>/',  CommentDetailView.as_view(), name='comment-detail'),
    # path('comment/create/', CommentCreateView.as_view(), name='comment-create'),

    path('comment/<int:pk>/', add_comment, name='add_comment'),
    path('all_posts/', posts_view, name='blog-home'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('user/<int:pk>/posts', user_posts, name='user_posts'),
    path('post/create/', post_create, name='post_create'),
    path('post/<int:pk>/update/', post_update, name='post_update'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>', tag_detail, name='tag_detail_url')
    ]

