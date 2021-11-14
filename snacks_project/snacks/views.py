from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



## views defined here


class HomePageView(TemplateView):
    template_name='home.html'

class AboutUsPageView(TemplateView):
    template_name='about_us.html'