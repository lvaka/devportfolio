# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from portfolio.models import Site
from portfolio.models import PortfolioImage
from django.http import JsonResponse

# Create your views here.
def home(request):

	sites = Site.objects.order_by('-pk')
	images = PortfolioImage.objects.order_by('-pk')

	return render (request, "portfolio/welcome.html", 
					{'sites':sites, 
					'images': images})

def portfolio_images(request):

	images = PortfolioImage.objects.order_by('-pk')
	data = {}

	for image in images:
		data['%s' % image.name] = image.image.url


	return JsonResponse(data)