from django.db import models

# candidate model
class Candidate(models.Model):
	# entries
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	skills = models.CharField(max_length=200)

	# for checking model
	def __str__(self):
		return self.name

# trainer model
class Trainer(models.Model):
	# entries
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	qualifications = models.CharField(max_length=200)

	# for checking model
	def __str__(self):
		return self.name

# company model
class Company(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	location = models.CharField(max_length=200)

	def __str__(self):
		return self.name

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