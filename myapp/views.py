from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic import (ListView ,
                                  DetailView , 
                                  CreateView,
                                  UpdateView,
                                  DeleteView
)
from .models import Post,book



def index(request) :
      
      return render(request , 'index.html')

def blogs(request):
      context= {
            'posts': Post.objects.all()
      }
      return render(request, 'blogs.html', context)

class PostListView(ListView):
      model = Post
      template_name='blogs.html'
      context_object_name= 'posts'
      ordering=['-date_posted']

class PostDetailView(DetailView):
      model = Post
      template_name = 'post_detail.html'



class PostCreateView(LoginRequiredMixin,CreateView):
      model = Post
      fields = ['title' , 'content']
      template_name = 'post_form.html'

      def form_valid(self,form):
            form.instance.author = self.request.user
            return super().form_valid(form)
      
      def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
      model = Post
      fields = ['title' , 'content']
      template_name = 'post_form.html'


      def form_valid(self,form):
            form.instance.author = self.request.user
            return super().form_valid(form)

      def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

      def test_func(self):
           Post=self.get_object()
           if self.request.user== Post.author:
                return True
           else:
                return False
           
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
      model = Post
      success_url= '/'
      template_name = 'post_confirm_delete.html'

      def test_func(self):
           Post=self.get_object()
           if self.request.user == Post.author:
                return True
           else:
                return False

def books(request):
      context_books= {
            'books': book.objects.all()
      }
      return render(request , 'books.html', context_books)