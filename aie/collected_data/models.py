from django.db import models
from datetime import datetime 
# Create your models here.
class EData(models.Model):
	userId = models.CharField(max_length=100)
	value = models.DecimalField(decimal_places=4, max_digits=15)
	date = models.DateTimeField(default=datetime.now)
	
	def __str__(self):
		return self.userId+' at: '+str(self.date)