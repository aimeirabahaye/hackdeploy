from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib import messages
import requests
import json
from django.shortcuts import render
from django.template import loader


def home(request):
    template = loader.get_template('home.html')

    response = requests.get("http://10.200.24.125:8000/api/worker")

    context = {"workers": json.loads(response.text)["results"]}

    return HttpResponse(template.render(context, request))

def posterHome(request):
    template = loader.get_template('posterhome.html')

    context = {}

    return HttpResponse(template.render(context, request))


def mePoster(request):
    template = loader.get_template('mePoster.html')

    response = requests.get("http://10.200.26.0:8000/api/poster/3")

    context = json.loads(response.text)
    
    return HttpResponse(template.render(context, request))

def posterInbox(request, posterID):
    template = loader.get_template('posterinbox.html')

    response = requests.get("http://10.200.26.0:8000/api/messages/")
    context = json.loads(response.text)
    messages = context["results"]
    context = {"messages":[]}

    for message in messages:
        print(message)
        d = {"task_id":message["task_id"],"message":message["message_content"]}
        workerResponse = requests.get("http://10.200.26.0:8000/api/worker/" + str(message["worker_id"]))
        worker = json.loads(workerResponse.text)
        d["worker"] = worker

        taskResponse = requests.get("http://10.200.26.0:8000/api/tasks/" + str(message["task_id"]))
        task = json.loads(taskResponse.text)
        d["task"] = task 
        context['messages'].append(d)

    return HttpResponse(template.render(context, request))

def showTask(request, ID):
    template = loader.get_template('showtask.html')

    response = requests.get("http://10.200.26.0:8000/api/tasks/" + str(ID))

    context = {"task":json.loads(response.text)}

    return HttpResponse(template.render(context, request))


def workerHome(request):
    template = loader.get_template('workerhome.html')

    response = requests.get("http://10.200.24.125:8000/api/worker")

    context = {"workers": json.loads(response.text)["results"]}

    return HttpResponse(template.render(context, request))


def workerProfile(request, profile_id):
    template = loader.get_template('workerProfile.html')

    response = requests.get(
        "http://10.200.26.0:8000/api/worker/" + str(profile_id))

    context = json.loads(response.text)

    return HttpResponse(template.render(context, request))


def createJob(request):
    if request.method=="POST":
        url = "http://10.200.26.0:8000/api/tasks/"
        job = request.POST
        requests.post(url, data = job)

    template = loader.get_template('createjob.html')

    response = requests.get("http://10.200.26.0:8000/api/tasks/")

    context = json.loads(response.text)
    tasks = context["results"]
    print(tasks)
    c = {"tasks": tasks}

    return HttpResponse(template.render(c, request))


def housekeeping(request):
    template = loader.get_template('housekeeping.html')

    response = requests.get("http://10.200.26.0:8000/api/tasks/")

    context = json.loads(response.text)["results"]

    c = {"tasks":[]}

    for task in context:
        if task["category"] == "HK":
            c["tasks"].append(task)

    return HttpResponse(template.render(c, request))

def education(request):
    template = loader.get_template('education.html')

    response = requests.get("http://10.200.26.0:8000/api/worker/")

    context = json.loads(response.text)

    return HttpResponse(template.render(context, request))

def technology(request):
    template = loader.get_template('technology.html')

    response = requests.get("http://10.200.26.0:8000/api/worker/")

    context = json.loads(response.text)

    return HttpResponse(template.render(context, request))

def animals(request):
    template = loader.get_template('animals.html')

    response = requests.get("http://10.200.26.0:8000/api/worker/")

    context = json.loads(response.text)

    return HttpResponse(template.render(context, request))

def repairs(request):
    template = loader.get_template('repairs.html')

    response = requests.get("http://10.200.26.0:8000/api/worker/")

    context = json.loads(response.text)

    return HttpResponse(template.render(context, request))

def delivery(request):
    template = loader.get_template('delivery.html')

    response = requests.get("http://10.200.26.0:8000/api/worker/")

    context = json.loads(response.text)

    return HttpResponse(template.render(context, request))

def entertainment(request):
    template = loader.get_template('entertainment.html')

    response = requests.get("http://10.200.26.0:8000/api/worker/")

    context = json.loads(response.text)

    return HttpResponse(template.render(context, request))
