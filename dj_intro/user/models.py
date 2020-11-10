from django.db import models

# Create your models here.
class Teacher(models.Model):

	USER_CHOICES = [
			('male', 'MALE'),
			('female', 'FEMALE')
		]

	name = models.CharField(max_length=100)
	sex = models.CharField(max_length=100, choices=USER_CHOICES)


	def __str__(self):
		return self.name
