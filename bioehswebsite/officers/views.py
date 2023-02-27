from django.shortcuts import render, redirect
from . import forms, models
from django.http import HttpResponseRedirect
from django.urls import reverse
import pprint
from . import utils
from home.models import SemesterSpecificInfo
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

def staff_required():
    return user_passes_test(lambda u: u.is_staff)

@staff_required()
@login_required
def site_documentation(request):
    return render(request, 'webmaster/documentation.html')

# Create your views here.
def default(request):
    latest_semester = list(forms.YearForm.sorted_semesters)[0]
    semester = str(latest_semester).replace(' ', '-')
    return redirect('detail', semester=semester)

def officersBySemester(request, semester):
    if request.method == 'GET':
        form = forms.YearForm()
    else:
        form = forms.YearForm(request.POST)
        if form.is_valid():
            submission = form.cleaned_data['semesters']
            semester = submission.replace(' ', '-')
            # print(semester)
            return redirect('detail', semester=semester)
        else:
            print('invalid')
    term, year = semester.split('-')
    year = int(year)
    semester_obj = models.Semester.semesters.get(term=term, year=year)
    execDetail = utils.officerDetailHTML(utils.execIterable, semester_obj)
    nonExecDetail = utils.officerDetailHTML(utils.nonExecIterable, semester_obj)
    assistantOfficersDetail = utils.officerDetailHTML(utils.assistantOfficersIterable, semester_obj)
    advisorsDetail = utils.officerDetailHTML(utils.advisorsIterable, semester_obj)
    return render(request, 'officers.html',
    {'form': form,
    'semester': semester.replace('-', ' '),
    'execDetail':execDetail,
    'nonExecDetail':nonExecDetail,
    'assistantOfficersDetail':assistantOfficersDetail,
    'advisorsDetail':advisorsDetail})

@login_required
def edit_user(request):
    pk = request.user.pk
    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)

    def generate_fields(user):
        if user.userprofile.is_officer:
            return ('image','linkedin')
        else:
            return None

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, can_delete=False, fields=(generate_fields(user)))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile/')

        return render(request, "accounts/update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied

@login_required
def alumni(request):
    all_urls = SemesterSpecificInfo.objects.first()
    return render(request, 'accounts/alumni.html', {'alumniDetailHTML': utils.alumniDetailHTML(), 'beacon_alum_registration': all_urls.beacon_alum_registration})
