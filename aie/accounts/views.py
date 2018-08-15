from django.shortcuts import render
from .models import Profile
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout, login

# Create your views here.
def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			return render(request, 'accounts/login.html', {'error': 'could not find user or user information incorrect'})
	else:
		return render(request, 'accounts/login.html')


def logout_view(request):
	logout(request)
	return render(request, 'accounts/logout.html')
