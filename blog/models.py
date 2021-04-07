from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

#Each class its going to be its own table in database
#Then in each class(DB table) we will add its attributes and datatypes
#auto_now=True  every time the feild is updated time is changed
#auto_now_add=True -> First time the feild(row) , that time is saved but this time can never be updated
#From django.utils import timezone then default=timezone.now allows us to change time only when we explicitly ask and not
# 	every time blog is updated

#We also have a author
# Author is the user adding the blog
# So details of author(that is user) should be mantained in another table that is class User
# From django.contrib.auth.models import User -> is added becaues django itself handles User table and we just have to 
# 	import it and include it in our Post class as a foreign key
# on_delete=models.CASCADE --> if the user is deleted their post will also be deleted

# In order to update database with any changes we need to run migrations 
#		Command(1)  ==python manage.py makemigrations
#		Command(2)  ==python manage.py migrate
#		Command(3)  ==python manage.py shell
#		Command(4)  ==from blog.models import Post
#		Command(5)  ==from django.contrib.auth.models import User
#		Command(6)  ==User.objects.all() /see all users
#		Command(7)  ==user = User.objects.filter(username = 'AreebaAkhtar').first() / AreebaAkhtar saved in var user
#		Command(8)  ==post_1 = Post(title = 'Blog 1' , content = 'First Blog Content' , author_id = user.id)
#		Command(9)  ==post_1.save()
#		Command(10) ==post = Post.objects.first()
#		Command(11) ==post.content
#make changes in views.py



class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk' : self.pk})	


class Contact(models.Model):
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=40)
	email = models.CharField(max_length=40)
	desc = models.TextField()
	time = models.DateTimeField(auto_now_add=True)