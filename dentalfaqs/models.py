from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

class Book(models.Model):
	your_name = models.CharField(max_length=100, primary_key=True)
	your_phone = models.CharField(max_length=100)
	your_email = models.CharField(max_length=100)
	your_address = models.CharField(max_length=100)
	Choose_your_slot = models.CharField(max_length=100)
	Choose_day = models.CharField(max_length=100)
	Choose_Doctor = models.CharField(max_length=100)
	Type_of_service = models.CharField(max_length=100)
	