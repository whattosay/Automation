from django.db import models

class User(models.Model):
	name = models.CharField(max_length=100)

class App(models.Model):
	name = models.CharField(max_length=100)

class Group(models.Model):
	name = models.CharField(max_length=100)

# Create your models here.
