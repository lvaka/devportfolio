# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from portfolio.models import Site, PortfolioImage

# Register your models here.
admin.site.register(Site)
admin.site.register(PortfolioImage)