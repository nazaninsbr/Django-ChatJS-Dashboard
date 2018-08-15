from django.shortcuts import render
from django.shortcuts import redirect
from .models import ContactMessage
from accounts.models import Profile
# Create your views here.
def contact_view(request):
	if not request.user.is_authenticated: 
		redirect('login')
	if request.method=='POST':
		sender = Profile.objects.filter(user=request.user)[0]
		subject = request.POST['subject']
		email = request.POST['email']
		body = request.POST['body']
		cm = ContactMessage(sender=sender, subject=subject, email=email, body=body)
		cm.save()
		return render(request, 'contact/submit_success.html')
	else:
		return render(request, 'contact/contact.html')
