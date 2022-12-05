from django.shortcuts import render
from django.views.generic import TemplateView
from . models import Venue


class DrvenuePageView(TemplateView):
    template_name = 'drvenue.html'


class BratsPageView(TemplateView):
    template_name = 'brats.html'


class MajesticPageView(TemplateView):
    template_name = 'majestic.html'


class BowlPageView(TemplateView):
    template_name = 'bowl.html'


class SylveePageView(TemplateView):
    template_name = 'sylvee.html'


class OrpheumPageView(TemplateView):
    template_name = 'orpheum.html'


class Venue_formPageView(TemplateView):
    template_name = 'venue_form.html'
