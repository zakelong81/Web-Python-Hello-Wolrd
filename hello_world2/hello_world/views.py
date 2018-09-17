# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


def index(request):
        helloworldviews = "CINS465 Hello World"
        return render(request, 'hellotmp/helloworld.html', {'helloworld': helloworldviews})
