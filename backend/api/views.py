from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Contact

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def contact(request):
    if request.method == "POST":
        req = json.loads(request.body)       

        first_name = req['first_name']
        last_name  = req['last_name']
        email      = req['email']
        phone      = req['phone']
        subject    = req['subject']
        comment    = req['comment']

        if first_name and email and subject and comment: 
            contact = Contact.objects.create(
                first_name = first_name,
                last_name  = last_name,
                email      = email,
                phone      = phone,
                subject    = subject,
                comment    = comment,
            )
            contact.save()
                        
            res = "success"            
            return JsonResponse({"msg": res}, status=201)
        else:
            res = "invalid request. Please fill required fields."
            return JsonResponse({"error": res}, status=400)