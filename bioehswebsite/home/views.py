from django.shortcuts import render, redirect
# Create your views here.
from .models import SemesterSpecificInfo

def apply(request):
    all_urls = SemesterSpecificInfo.objects.first()
    regular_application_form = all_urls.regular_application_form
    prospective_member_interest_form = all_urls.prospective_member_interest_form
    return render(request, 'about/apply.html', {'regular_application_form':regular_application_form, 'prospective_member_interest_form':prospective_member_interest_form})

def quicklink_overview(request):
    return redirect('/bioehsc/')

def overview(request):
    all_urls = SemesterSpecificInfo.objects.first()
    bioehsc_poster_link = all_urls.bioehsc_poster_link
    return render(request, 'bioehsc/bioehsc.html', {'bioehsc_poster_link':bioehsc_poster_link})

def bioe(request):
    all_urls = SemesterSpecificInfo.objects.first()
    outreach_blog = all_urls.outreach_blog
    return render(request, 'bioehsc/bioe.html', {'outreach_blog': outreach_blog})

def timeline(request):
    all_urls = SemesterSpecificInfo.objects.first()
    return render(request, 'bioehsc/timeline.html',
    {'bioehsc_progress_form': all_urls.bioehsc_progress_form,
    'bioehsc_handbook': all_urls.bioehsc_handbook,
    'bioehsc_handbook_feedback_form': all_urls.bioehsc_handbook_feedback_form,
    'bioehsc_video_abstract_example_videos': all_urls.bioehsc_video_abstract_example_videos,
    'bioehsc_resources_drive': all_urls.bioehsc_resources_drive,
    'bioehsc_poster_examples': all_urls.bioehsc_poster_examples,
    'campus_map': all_urls.campus_map})

def registration(request):
    all_urls = SemesterSpecificInfo.objects.first()
    return render(request, 'bioehsc/registration.html',
    {'bioehsc_online_application': all_urls.bioehsc_online_application,
    'bioehsc_petition_form': all_urls.bioehsc_petition_form,
    'bioehsc_liability_form': all_urls.bioehsc_liability_form,
    'bioehsc_photo_release_form': all_urls.bioehsc_photo_release_form,
    'bioehsc_medical_auth_form': all_urls.bioehsc_medical_auth_form,
    'bioehsc_school_auth_form': all_urls.bioehsc_school_auth_form,
    'bioehsc_student_registration_form': all_urls.bioehsc_student_registration_form,
    'bioehsc_fee_waiver': all_urls.bioehsc_fee_waiver,
    'bioehsc_parent_release_form': all_urls.bioehsc_parent_release_form,
    'bioehsc_paperwork_documentation': all_urls.bioehsc_paperwork_documentation,
    'bioehsc_non_student_registration_form': all_urls.bioehsc_non_student_registration_form,
    'bioehsc_hs_flyer':all_urls.bioehsc_hs_flyer
    })

def outreach(request):
    all_urls = SemesterSpecificInfo.objects.first()
    return render(request, 'committees/outreach.html', {'bioe_day_rsvp_form': all_urls.bioe_day_rsvp_form, 'outreach_blog':all_urls.outreach_blog, 'bioe_day_flyer':all_urls.bioe_day_flyer})

def volunteer(request):
    all_urls = SemesterSpecificInfo.objects.first()
    return render(request, 'bioehsc/volunteer.html', {'bioehsc_volunteer_flyer':all_urls.bioehsc_volunteer_flyer, 'undergrad_form':all_urls.bioehsc_ugrad_volunteer,
    'grad_form': all_urls.bioehsc_grad_volunteer,
    'undergrad_mentor_form':all_urls.bioehsc_ugrad_mentor,
    'industry_form': all_urls.bioehsc_industry_volunteer,
    'faculty_form': all_urls.bioehsc_faculty_volunteer})
