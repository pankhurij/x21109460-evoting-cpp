from django.db import models

# Create your models here.

class PollQuestion(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text


class Parties(models.Model):
	question = models.ForeignKey(PollQuestion, on_delete = models.CASCADE)
	choice = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	def __str__(self):
		return self.choice
