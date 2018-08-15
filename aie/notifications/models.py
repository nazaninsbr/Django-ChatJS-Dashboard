from django.db import models
from collected_data.models import EData
from accounts.models import Profile
# Create your models here.
class Norm(models.Model):
	value = models.DecimalField(decimal_places=2, max_digits=15)
	start_hour = models.TimeField(unique=True)
	end_hour = models.TimeField()

	def __str__(self):
		return 'normal usage from: '+self.start_hour.strftime('%H:%M:%S')+' to '+self.end_hour.strftime('%H:%M:%S')


class Notif(models.Model):
	for_user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
	for_data = models.ForeignKey(EData, on_delete=models.DO_NOTHING)

	def __str__(self):
		return "A warning for user: "+self.for_user.user.username