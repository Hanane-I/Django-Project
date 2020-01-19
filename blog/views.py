from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.views.generic import(
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'

class PostDetailView(DetailView):
	model = Post
	
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','texte','photo','tags']

	def form_valid(self,form):
		return super().form_valid(form)
		


class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Post
	fields = ['title','texte','photo','tags']

	def form_valid(self,form):
		return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = Post 
	success_url = '/'

def about(request):
	return render(request,'blog/about.html')
