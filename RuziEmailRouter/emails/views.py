from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail

@csrf_exempt
def index(request):
	if request.method == 'GET':
		print("That's not supposed to happen!!")
	elif request.method == 'POST':
		jsonContents = json.loads(request.body)
		print(jsonContents)

		try:
			sender = "Michael.B.Kolbeck@gmail.com"
			receivers = [jsonContents.get('driverEmail')]
			message = "This is a test message."
			send_mail('Subject',message,sender,receivers,fail_silently=False)
		except Exception as e:
			print("Did you remember to update settings.py with your actual password?")
			print(e)

		return HttpResponse("Hello from the email receiver, you sent over:\n" + request.body.decode("utf-8"))

# Create your views here.
