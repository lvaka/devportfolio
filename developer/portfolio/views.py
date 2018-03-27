# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Site

# Create your views here.
def home(request):

	sites = Site.objects.order_by('-pk')

	return render (request, "portfolio/welcome.html", {'sites':sites})