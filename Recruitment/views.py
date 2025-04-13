from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Candidate

def index(request):
    return HttpResponse("Recruitment page.")

def account(request, candidate_id):
    output = Candidate.objects.get(pk=1)
    template = loader.get_template("recruitment/index.html")
    context = {"user": output}
    return HttpResponse(template.render(context, request))
