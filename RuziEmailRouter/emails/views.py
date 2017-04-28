from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
	if request.method == 'GET':
		print("That's not supposed to happen!!")
	elif request.method == 'POST':
#		print(request.body)
		print(json.loads(request.body))
		return HttpResponse("Hello from the email receiver, you sent over:\n" + request.body.decode("utf-8"))

# Create your views here.
