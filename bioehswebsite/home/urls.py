"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('bioehsc/', views.overview, name='bioehsc'),
    path('hsc/', views.quicklink_overview, name='bioehsc_quick'),
    path('bioehsc/timeline/', views.timeline, name='timeline'),
    path('bioehsc/faq/', TemplateView.as_view(template_name='bioehsc/faq.html'), name='faq'),
    path('donate/', TemplateView.as_view(template_name='donate.html'), name='donate'),
    path('privacy/', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    path('terms/', TemplateView.as_view(template_name='terms.html'), name='terms'),
    path('decal/overview/', TemplateView.as_view(template_name='decal/overview.html'), name='overview'),
    path('decal/team/', TemplateView.as_view(template_name='decal/team.html'), name='team'),
    path('decal/syllabus/', TemplateView.as_view(template_name='decal/syllabus.html'), name='syllabus'),
    path('committees/outreach/', views.outreach, name='outreach'),
    path('committees/academic/', TemplateView.as_view(template_name='committees/academic.html'), name='academic'),
    path('committees/prodev/', TemplateView.as_view(template_name='committees/prodev.html'), name='prodev'),
    path('committees/projects/', TemplateView.as_view(template_name='committees/projects.html'), name='projects'),
    path('bioehsc/archives/', TemplateView.as_view(template_name='bioehsc/archives.html'), name='archives'),
    path('bioehsc/registration/', views.registration, name='registration'),
    path('bioehsc/bioe/', views.bioe, name='bioehsc_bioe'),
    path('bioehsc/requirements/', TemplateView.as_view(template_name='bioehsc/requirements.html'), name='bioehsc_requirements'),
    path('bioehsc/volunteer/', views.volunteer, name='bioehsc_volunteer'),
    path('about/apply/', views.apply, name='apply'),
    path('studentservices/coursemap/', TemplateView.as_view(template_name='studentservices/coursemap.html'), name='coursemap'),
    path('courseguides/math1a', TemplateView.as_view(template_name='courseguides/math1a.html'), name='math1a'),
    path('courseguides/math1b', TemplateView.as_view(template_name='courseguides/math1b.html'), name='math1b'),
    path('courseguides/math53', TemplateView.as_view(template_name='courseguides/math53.html'), name='math53'),
    path('courseguides/math54', TemplateView.as_view(template_name='courseguides/math54.html'), name='math54'),
    path('courseguides/physics7a', TemplateView.as_view(template_name='courseguides/physics7a.html'), name='physics7a'),
    path('courseguides/physics7b', TemplateView.as_view(template_name='courseguides/physics7b.html'), name='physics7b'),
    path('courseguides/e7', TemplateView.as_view(template_name='courseguides/e7.html'), name='e7'),
    path('courseguides/cs61a', TemplateView.as_view(template_name='courseguides/cs61a.html'), name='cs61a'),
    path('courseguides/cs61b', TemplateView.as_view(template_name='courseguides/cs61b.html'), name='cs61b'),
    path('courseguides/cs70', TemplateView.as_view(template_name='courseguides/cs70.html'), name='cs70'),
    path('courseguides/data100', TemplateView.as_view(template_name='courseguides/data100.html'), name='data100'),
    path('courseguides/chem3a', TemplateView.as_view(template_name='courseguides/chem3a.html'), name='chem3a'),
    path('courseguides/chem3al', TemplateView.as_view(template_name='courseguides/chem3al.html'), name='chem3al'),
    path('courseguides/chem3b', TemplateView.as_view(template_name='courseguides/chem3a.html'), name='chem3b'),
    path('courseguides/chem3bl', TemplateView.as_view(template_name='courseguides/chem3bl.html'), name='chem3bl'),
    path('courseguides/bio1a', TemplateView.as_view(template_name='courseguides/bio1a.html'), name='bio1a'),
    path('courseguides/bioe10', TemplateView.as_view(template_name='courseguides/bioe10.html'), name='bioe10'),
    path('courseguides/bioe11', TemplateView.as_view(template_name='courseguides/bioe11.html'), name='bioe11'),
    path('courseguides/bioe100', TemplateView.as_view(template_name='courseguides/bioe100.html'), name='bioe100'),
    path('courseguides/bioe101', TemplateView.as_view(template_name='courseguides/bioe101.html'), name='bioe101'),
    path('courseguides/bioe102', TemplateView.as_view(template_name='courseguides/bioe102.html'), name='bioe102'),
    path('courseguides/bioe103', TemplateView.as_view(template_name='courseguides/bioe103.html'), name='bioe103'),
    path('courseguides/bioe104', TemplateView.as_view(template_name='courseguides/bioe104.html'), name='bioe104'),
    path('courseguides/bioe105', TemplateView.as_view(template_name='courseguides/bioe105.html'), name='bioe105'),
    path('courseguides/bioe110', TemplateView.as_view(template_name='courseguides/bioe110.html'), name='bioe110'),
    path('courseguides/bioe115', TemplateView.as_view(template_name='courseguides/bioe115.html'), name='bioe115'),
    path('courseguides/bioe116', TemplateView.as_view(template_name='courseguides/bioe116.html'), name='bioe116'),
    path('courseguides/bioec117', TemplateView.as_view(template_name='courseguides/bioec117.html'), name='bioec117'),
    path('courseguides/bioec118', TemplateView.as_view(template_name='courseguides/bioec118.html'), name='bioec118'),
    path('courseguides/bioec119', TemplateView.as_view(template_name='courseguides/bioec119.html'), name='bioec119'),
    path('courseguides/bioe121', TemplateView.as_view(template_name='courseguides/bioe121.html'), name='bioe121'),
    path('courseguides/bioe121l', TemplateView.as_view(template_name='courseguides/bioe121l.html'), name='bioe121l'),
    path('courseguides/bioe124', TemplateView.as_view(template_name='courseguides/bioe124.html'), name='bioe124'),
    path('courseguides/bioe131', TemplateView.as_view(template_name='courseguides/bioe131.html'), name='bioe131'),
    path('courseguides/bioe134', TemplateView.as_view(template_name='courseguides/bioe134.html'), name='bioe134'),
    path('courseguides/bioe135', TemplateView.as_view(template_name='courseguides/bioe135.html'), name='bioe135'),
    path('courseguides/bioe140l', TemplateView.as_view(template_name='courseguides/bioe140l.html'), name='bioe140l'),
    path('courseguides/bioe145', TemplateView.as_view(template_name='courseguides/bioe145.html'), name='bioe145'),
    path('courseguides/bioe147', TemplateView.as_view(template_name='courseguides/bioe147.html'), name='bioe147'),
    path('courseguides/bioe148', TemplateView.as_view(template_name='courseguides/bioe148.html'), name='bioe148'),
    path('courseguides/bioe151', TemplateView.as_view(template_name='courseguides/bioe151.html'), name='bioe151'),
    path('courseguides/bioec157', TemplateView.as_view(template_name='courseguides/bioec157.html'), name='bioec157'),
    path('courseguides/bioe166', TemplateView.as_view(template_name='courseguides/bioe166.html'), name='bioe166'),
    path('courseguides/bioe171', TemplateView.as_view(template_name='courseguides/bioe171.html'), name='bioe171'),
    path('courseguides/bioe196', TemplateView.as_view(template_name='courseguides/bioe196.html'), name='bioe196'),
    path('courseguides/mcbc100a', TemplateView.as_view(template_name='courseguides/mcbc100a.html'), name='mcbc100a'),
    path('courseguides/chem3a', TemplateView.as_view(template_name='courseguides/chem3a.html'), name='chem3a'),
    path('professors/terryjohnson', TemplateView.as_view(template_name='professors/terryjohnson.html'), name='terryjohnson'),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
