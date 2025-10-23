from django.urls import path
from my_blog import views

urlpatterns = [
    path('',views.AboutView.as_view(),name='post_list'),
    path('about/',views.PostListView.as_view(),name='about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_new'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_new'),
]
