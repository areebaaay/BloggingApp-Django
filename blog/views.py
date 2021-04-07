# from django.shortcuts import render
# from django.http import HttpResponse
# #This function will help to handle the traffic from our homepage of blog
# def Home(request):
# 	render HttpResponse(<h1>Blog Home</h1>)
# #Map URL pattern to view Home fuction and hence a url.py file is created by Areeba in blog folder

# # Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post, Contact
from django.core.mail import send_mail
from django.conf import settings
# Post is the table we created in models,py

#creating some dummy data lets say about dictionary
# posts = [
# 	{
# 		'author' : 'CoreyMS' ,
# 		'title' : 'Blog Post 1' ,
# 		'content' : 'First Post Content' ,
# 		'date posted' : '11 Nov, 2020'
# 	},
# 	{
# 		'author' : 'Jane Doe' ,
# 		'title' : 'Blog Post 2' ,
# 		'content' : 'Second Post Content' ,
# 		'date_posted' : '12 Nov, 2020'
# 	}
# ]


	#creating a dictionry named context and a key in context called posts
	#passing the dummy data posts(author title) to the key we created 'posts'
def home(request):
	context = {
	        #'posts': posts
	        'posts' : Post.objects.all()
	    }


	#now with the keyword posts we can access the data on our template(considering that data came from a database)


class PostListView(ListView):
	model  =  Post
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] #order of blog newest to oldest
	paginate_by = 5

class UserPostListView(ListView):
	model  =  Post
	template_name = 'blog/user_post.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
#	ordering = ['-date_posted'] #order of blog newest to oldest
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model  =  Post
	
class PostCreateView(LoginRequiredMixin, CreateView):
	model  =  Post
	fields = [ 'title', 'content']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model  =  Post
	fields = [ 'title', 'content']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False	

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model  =  Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False	

def about(request):
	return render (request,'blog/about.html', {'title' : 'About'})

def additional(request):
	return render (request,'blog/additional.html', {'title' : 'Additional'})	

def contact(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		desc = request.POST.get("desc")
		instance = Contact(name=name, email=email, desc=desc)
		instance.save()

		# desc = request.POST['desc']
		# send_mail('Contact Form',
		# 	desc,
		# 	settings.EMAIL_HOST_USER,
		# 	['areeba.akhtar776@gmail.com'],
		# 	fail_silently=False)

		message = request.POST['email'] + "\n " + request.POST['desc'] 
		send_mail('Contact Form',
			message,
			settings.EMAIL_HOST_USER,
			['areeba.akhtar776@gmail.com'],
			fail_silently=False)

		
	return render(request, 'blog/contact.html' , {'title' : 'Contact'})	


def search(request):
	query = request.GET.get('query')
	posts = Post.objects.filter(title__icontains=query).order_by('-date_posted')
	params = {'posts' : posts}
	return render(request, 'blog/search.html' , params)
	#return HttpResponse('This is search')

#blog -> templates -> blog -> template.html
#we had a blog directory(python manage.py startapp blog)
#in that directory we created a templates directory(right click blog new folder)
#in blog ->templates directory we created a blog directory(right click templates new folder)
#in blog -> templates -> blog directory we created a template.html file(right click blog new file)
