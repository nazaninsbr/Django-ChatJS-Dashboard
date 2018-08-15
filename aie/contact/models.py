from django.db import models
from accounts.models import Profile
# Create your models here.

class ContactMessage(models.Model):
	sender = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
	subject = models.CharField(max_length=200)
	email = models.EmailField()
	body = models.TextField()

	def __str__(self):
		return 'From: '+self.sender.user.username+' Title: '+self.subject