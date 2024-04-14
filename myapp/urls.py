from django.urls import path , include
from .views import (PostListView , 
                    PostDetailView , 
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView
)

from . import views

urlpatterns = [
path('', PostListView.as_view() , name='index'),
path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
path('post/<int:pk>/update/', PostUpdateView.as_view() , name='post-update'),
path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='post-delete'),
path('post/new/', PostCreateView.as_view() , name='post-create'),
path('blogs/', views.blogs , name='blogs'),
path('books/' , views.books , name='books'),
]