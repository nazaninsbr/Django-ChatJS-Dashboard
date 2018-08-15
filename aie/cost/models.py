from django.db import models

# Create your models here.
class CostBasedOnHour(models.Model):
	start_hour = models.TimeField(unique=True)
	end_hour = models.TimeField()
	border_value = models.DecimalField(decimal_places=2, max_digits=15)
	cost_below = models.DecimalField(decimal_places=2, max_digits=15)
	cost_above = models.DecimalField(decimal_places=2, max_digits=15)

	def __str__(self):
		return 'cost from: '+self.start_hour.strftime('%H:%M:%S')+' to '+self.end_hour.strftime('%H:%M:%S')