import email
from queue import Empty
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Creator
from myapp import models

GET = "GET"
POST = "POST"

def index(request):
    response = '''
    <!doctype html>
    <html>
    <head>
        <title>This is the title of the webpage!</title>
    </head>
    <body>
        <p>This is an example paragraph. Anything in the <strong>body</strong> tag will appear on the page, just like this <strong>p</strong> tag and its contents.</p>
    </body>
    </html>
    '''
    return HttpResponse(response)

@csrf_exempt
def create_creator(request):
    if request.method == POST:
        name = request.GET.get("name", "")
        nickname = request.GET.get("nickname", "")
        email = request.GET.get("email", "")

        if Creator.objects.filter(nickname=nickname).exists():
            return JsonResponse({"message" : "creator does already exist"})
        
        # Сохраняем в базу данных
        creator = Creator(name=name, nickname=nickname, email=email)
        creator.save()

        return JsonResponse({"nickname": nickname})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")

def read_creator_by_id(request, creator_id):
    if request.method == GET:
        try:
            creator = models.Creator.objects.get(id=creator_id)

            return JsonResponse(
                {
                    "id": creator.id, 
                    "name": creator.name, 
                    "nickname": creator.nickname, 
                    "email": creator.email
                }
            )
        except models.Creator.DoesNotExist:
            return JsonResponse({"message" : "creator does not exist"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")

@csrf_exempt
def delete_creator_by_nikname(request, nickname):
    if request.method == POST:
        Creator.objects.filter(nickname=nickname).delete()

        return JsonResponse({"nickname": nickname})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")