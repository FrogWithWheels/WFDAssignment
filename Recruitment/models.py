from django.db import models

# Create your models here.
class Candidate(models.Model):
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	dob = models.DateTimeField()

	def __str__(self):
		return self.name

class Trainer(models.Model):
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)

	def __str__(self):
		return self.name