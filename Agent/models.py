from django.db import models

# Create your models here.
class Issue(models.Model):
	issue=models.CharField(max_length=100,blank=False) 

class PredictAgent(models.Model):
	agent = models.CharField(max_length=50,blank=False)
	abandoned=models.ForeignKey(Issue, on_delete=models.CASCADE)
	abandoned_time = models.DateTimeField(max_length=50, null=True,blank=True)
	start_time = models.DateTimeField(max_length=50, null=True)
	answer_time = models.DateTimeField(max_length=50, null=True)
	resolved=models.CharField(max_length=100, null=False, default='N/A')
	resolved_time = models.DateTimeField(max_length=50, null=True,blank=True)
	def __str__(self):
		return self.agent