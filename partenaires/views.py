from django.template import RequestContext, loader
from partenaires.models import Partenaires
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response


def index(request):
    partenaires_list = Partenaires.objects.all()
    return render_to_response('partenaires/partenaires.html',
        RequestContext(request, {'partenaires': partenaires_list}))

# Create your views here.
