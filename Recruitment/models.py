# imports
from django.db import models
from django.contrib.auth.models import AbstractUser

# abstract user that others extend from
class UserModel(AbstractUser):
	USER_TYPES = (
		("CANDIDATE", "candidate"),
		("TRAINER", "trainer"),
		("COMPANY", "company"),
	)
	email = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)

	# for checking model
	def __str__(self):
		return self.username

# candidate model
class Candidate(models.Model):
	# entries
	user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
	skills = models.CharField(max_length=200)

# trainer model
class Trainer(models.Model):
	# entries
	user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
	qualifications = models.CharField(max_length=200)

# company model
class Company(models.Model):
	user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)

# job model
class Job(models.Model):
	# entries
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	salary = models.CharField(max_length=200)
	status = models.CharField(max_length=200)
	date = models.DateTimeField("Date")

	# foreign key
	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	# for checking model
	def __str__(self):
		return self.name

# training model
class Training(models.Model):
	# entries
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	qualification = models.CharField(max_length=200)
	duration = models.CharField(max_length=200)
	date = models.DateTimeField("Date")

	# foreign key
	trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

	# for checking model
	def __str__(self):
		return self.name

# enrollment model
class Enrollment(models.Model):
	# entries
	status = models.CharField(max_length=200)
	date = models.DateTimeField("Date")

	# foreign keys
	trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

	# for checking model
	def __str__(self):
		return self.name

# application model
class Application(models.Model):
	# entries
	status = models.CharField(max_length=200)
	date = models.DateTimeField("Date")

	# foreign keys
	trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
	job = models.ForeignKey(Job, on_delete=models.CASCADE)

	# for checking model
	def __str__(self):
		return self.name

