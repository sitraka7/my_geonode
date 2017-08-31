from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views



urlpatterns = patterns('partenaires.views',
   url(r'^$',
       TemplateView.as_view(template_name='partenaires/partenaires.html'),
       name='partenaires'),
    )

