from django.shortcuts import render, redirect
from . import models
from .models import Year, Sponsor
from django.http import HttpResponseRedirect
from django.urls import reverse
import pprint
from . import utils
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


# Create your views here.


def index(request):
	sponsors = Sponsor.objects.all()
	years_list = Year.objects.all()
	sponsorDetail = "<br></br>"
	for year in Year.objects.all().order_by('-year'):
		sponsorDetail += "<h4 class='display-4' style='text-align: center;'>" + str(year) + " Sponsors</h4>"
		sponsorDetail += utils.sponsorDetailHTML(year)
		sponsorDetail += "<br> </br>"

	context = {
		'sponsorDetail':sponsorDetail
	}
	return render(request, 'industrialrel.html', context=context)
