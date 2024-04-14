from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content= models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    def get_absoulute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class book(models.Model):
    book_title = models.CharField(max_length=100)
    book_price=models.CharField(max_length=15,default='')
    book_content=models.TextField()
    book_date_posted=models.DateTimeField(default=timezone.now)
    book_author=models.ForeignKey(User, on_delete=models.CASCADE)
    book_picture = models.ImageField(upload_to='book/picture' , null=True , blank=True)

    def __str__(self):
        return self.book_title