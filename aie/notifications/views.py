from django.shortcuts import render
from .models import Norm, Notif
from collected_data.models import EData
from accounts.models import Profile
# Create your views here.

def getTimeStr(o):
	TIME_FORMAT = "%H:%M:%S"
	return o.strftime(TIME_FORMAT)


def getAllDataAboveNorm(edata):
	norms = Norm.objects.all()
	result = []
	for data in edata:
		for norm in norms:
			if getTimeStr(data.date) > getTimeStr(norm.start_hour) and getTimeStr(data.date) < getTimeStr(norm.end_hour):
				if data.value > norm.value:
					result.append(data)
	return result


def getNewOnes(edata):
	all_notifs = Notif.objects.all()
	found = 0
	result = []
	for data in edata:
		for notif in all_notifs:
			if notif.for_data==data:
				found = 1
				break
		if found==0:
			result.append(data)
		elif found==1:
			found = 0
	return result


def notifications_view(request):
	if not request.user.is_authenticated:
		return redirect('login')

	profile = Profile.objects.filter(user=request.user)[0]
	edata = EData.objects.filter(userId=profile.id)

	above_norm = getAllDataAboveNorm(edata)
	new_data = getNewOnes(above_norm)

	for data in new_data:
		nf = Notif(for_user=profile, for_data=data)
		nf.save()

	all_notifications = Notif.objects.all()
	content = {'notifs':all_notifications}
	return render(request, 'notifications/index.html', content)
	

