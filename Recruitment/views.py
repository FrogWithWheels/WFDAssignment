from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.contrib import auth, messages
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

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.method = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'registration/account.html')
        else:
            messages.info(request, "invalid credentials")
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')
