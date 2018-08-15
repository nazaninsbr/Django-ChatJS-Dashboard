from django.shortcuts import render
from .models import EData
# Create your views here.
def get_data_view(request):
	if request.method=='POST':
		userId = request.POST['id']
		value = request.POST['value']
		edata = EData(userId=userId, value=value)
		edata.save()
		return render(request, "collect/get_data.html")
	else:
		return render(request, "collect/get_data.html")
