from queue import Empty
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

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

def film_by_id(request, film_id):
    if request.method == GET:
        # read from db
        return JsonResponse({"film_name": "film_name", "status": "OK"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")

def read_film(request):
    if request.method == GET:
        film_id = request.GET.get("film_id", "")
        name = request.GET.get("name", "")
        genre = request.GET.get("genre", "")
        return JsonResponse({"film_id": film_id, "name": name, "genre": genre})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")

@csrf_exempt
def update_film(request):
    if request.method == POST:
        film_id = request.POST.get("film_id", "")
        name = request.POST.get("name", "")
        genre = request.POST.get("genre", "")
        # Сохраняем в базу данных
        return JsonResponse({"film_id": film_id, "status": "OK"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")