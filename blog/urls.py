from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
]
