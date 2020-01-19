from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	texte = models.TextField()
	photo = models.ImageField(default='pic1.png', upload_to='profile_pics')
	tags = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
