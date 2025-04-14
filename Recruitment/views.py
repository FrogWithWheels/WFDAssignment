from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Candidate

# index page 
def index(request):
    return HttpResponse("Recruitment page.")

# page for displaying account information
def account(request, candidate_id):
    # saving specific user to variable
    output = get_object_or_404(Candidate, pk=candidate_id)

    # loading the template
    template = loader.get_template("recruitment/index.html")

    # loading context to send to template
    context = {"user": output}

    # displaying page
    return HttpResponse(template.render(context, request))
