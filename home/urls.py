from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    tags_list,
    tag_detail,
    TagCreate,
    view_home,
    page_home,
    add_comment,
    # CommentListView,
    # CommentDetailView,
    # CommentCreateView,

)

app_name = 'home'


urlpatterns = [
    path('', page_home, name='page_home'),
    # path('comment/',  CommentListView.as_view(), name='comment'),
    # path('comment/<int:pk>/',  CommentDetailView.as_view(), name='comment-detail'),
    # path('comment/create/', CommentCreateView.as_view(), name='comment-create'),

    path('comment/<int:pk>/', add_comment, name='add_comment'),

    path('view_home/', view_home, name='view_home'),
    path('all_posts', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>', tag_detail, name='tag_detail_url')
    ]
