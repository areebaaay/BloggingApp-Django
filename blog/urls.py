# from django.urls import path #this statement is also present in django_projects file urls.py
# from . import views
# urlpatterns = [
#     path('', views.home, name='blog-home'),
# ] #this is also from urls.py but necressary changes are made like admin/ is removed bc we dont want to go in admin directory
# #views.home=home view from views module
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about, name='blog-about'),
    path('additional/',views.additional, name='blog-additional'),
    path('search/',views.search, name='search'),
    path('contact/',views.contact, name='contact')
]



# 'post/<int:pk>/' pk=primary key. this is for the time when i click blog 1 then post/1 should open