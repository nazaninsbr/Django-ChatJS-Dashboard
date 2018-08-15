from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	country = models.CharField(max_length=25, default='Iran')
	city = models.CharField(max_length=50, default='Tehran')
	district = models.IntegerField()
	number_of_people_in_the_household = models.IntegerField()
	number_of_rooms = models.IntegerField()
	joined_on = models.DateField()

	def __str__(self):
		return self.user.first_name+' '+self.user.last_name