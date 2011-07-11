from django.db import models

class University(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField('date added')
	
	def __unicode__(self):
		return self.name
