from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.http import JsonResponse

from django.contrib.auth.models import User
from collected_data.models import EData
from accounts.models import Profile
from cost.models import CostBasedOnHour
import datetime 
import json
# Create your views here.

def getDate(o):
	DATE_FORMAT = "%Y-%m-%d"
	return o.strftime(DATE_FORMAT)

def getTimeStr(o):
	TIME_FORMAT = "%H:%M:%S"
	return o.strftime(TIME_FORMAT)


def getTodaysTotalUsage(edata):
	today_usage_sum = 0
	for data in edata:
		if getDate(data.date)==datetime.datetime.today().strftime('%Y-%m-%d'):
			today_usage_sum += float(data.value)
	return '%.2f' % today_usage_sum

def getTodaysCost(edata):
	todays_cost = 0
	costs = CostBasedOnHour.objects.all()
	for data in edata:
		for cost in costs:
			if getTimeStr(data.date) > getTimeStr(cost.start_hour) and getTimeStr(data.date) < getTimeStr(cost.end_hour):
				if data.value > cost.border_value:
					todays_cost = data.value*cost.cost_below
				else:
					todays_cost = data.value*cost.cost_above
	return '%.2f' % todays_cost

def getWeeksTotalCost(request):
	profile = Profile.objects.filter(user=request.user)[0]
	
	date = datetime.date.today()
	start_week = date - datetime.timedelta(date.weekday())
	end_week = start_week + datetime.timedelta(7)
	
	edata = EData.objects.filter(userId=profile.id, date__range=[start_week, end_week])

	week = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[], "Sunday":[]}
	for data in edata:
		week[data.date.strftime("%A")].append(data)

	costs = []
	for key in week.keys():
		s = float(getTodaysCost(week[key]))
		costs.append(s)

	costSum = sum(costs[0:len(costs)])
	return '%.2f' % costSum

def getWeekAverage(request):
	profile = Profile.objects.filter(user=request.user)[0]
	
	date = datetime.date.today()
	start_week = date - datetime.timedelta(date.weekday())
	end_week = start_week + datetime.timedelta(7)
	
	edata = EData.objects.filter(userId=profile.id, date__range=[start_week, end_week])

	week = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[], "Sunday":[]}
	for data in edata:
		week[data.date.strftime("%A")].append(data.value)

	sums = []
	for key in week.keys():
		s = float(sum(week[key][0:len(week[key])]))
		sums.append(s)

	average = sum(sums[0:len(sums)])/len(sums)
	return '%.2f' % average

def home(request):
	if not request.user.is_authenticated:
		return redirect('login')

	profile = Profile.objects.filter(user=request.user)[0]
	edata = EData.objects.filter(userId=profile.id)
	
	content = {'today_usage':getTodaysTotalUsage(edata), 'today_cost': getTodaysCost(edata), 'this_week_average': getWeekAverage(request), 'this_week_cost':getWeeksTotalCost(request)}
	return render(request, 'panel/index.html', content)

def convertDateTimeToString(o):
	DATE_FORMAT = "%Y-%m-%d"
	TIME_FORMAT = "%H:%M:%S"
	
	if isinstance(o, datetime.datetime):
		return o.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))
	elif isinstance(o, datetime.date):
		return o.strftime(DATE_FORMAT)

def get_week_data(request, *args, **kwargs):
	profile = Profile.objects.filter(user=request.user)[0]
	
	date = datetime.date.today()
	start_week = date - datetime.timedelta(date.weekday())
	end_week = start_week + datetime.timedelta(7)
	
	edata = EData.objects.filter(userId=profile.id, date__range=[start_week, end_week])

	week = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[], "Sunday":[]}
	for data in edata:
		week[data.date.strftime("%A")].append(data.value)

	sums = []
	for key in week.keys():
		s = float(sum(week[key][0:len(week[key])]))
		sums.append(s)

	data = {
		"values": sums,
	}
	return JsonResponse(json.dumps(data), safe=False)


def get_all_time_data(request, *args, **kwargs):
	profile = Profile.objects.filter(user=request.user)[0]
	edata = EData.objects.filter(userId=profile.id)
	all_time_usage = []
	all_time_dates = []
	for data in edata:
		# all_time_usage.append({'x': convertDateTimeToString(data.date), 'y':float(data.value)})
		all_time_usage.append(float(data.value))
		all_time_dates.append(convertDateTimeToString(data.date))
	data = {
		"values": all_time_usage,
		"dates": all_time_dates 
	}
	return JsonResponse(json.dumps(data), safe=False)


