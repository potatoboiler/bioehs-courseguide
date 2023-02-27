from django.db import models

# Create your models here.
class SemesterSpecificInfo(models.Model):
    class Meta:
        verbose_name = 'Semester Specific Information'
        verbose_name_plural = 'Semester Specific Information/Resources'
    campus_map = models.ImageField('Campus Map', default='campusmap.jpg', upload_to='', help_text='TO BE UPDATED EACH SPRING')
    decal_flyer = models.URLField('Decal Flyer', default='https://drive.google.com/file/d/1--Z7TlbzwTaXhan4slS_kY8ajyi3RSHR/view?usp=sharingupload_to=', help_text='TO BE UPDATED EACH FALL')
    regular_application_form = models.URLField('Regular Application Form', default='https://tinyurl.com/Sp21application', help_text='TO BE UPDATED EACH SEMESTER')
    prospective_member_interest_form = models.URLField('Prospective Member Interest Form', default='https://docs.google.com/forms/d/e/1FAIpQLSeunglCnYuYMrjm_3eLgSTgCfEEMZL99J06VcgwN0gKhVX6Wg/viewform', help_text='TO BE UPDATED EACH SEMESTER')
    outreach_blog = models.URLField('Outreach Blog', default='https://bioehs.wordpress.com/', help_text='Check with Outreach if this needs to be updated')
    bioehsc_progress_form = models.URLField('BioEHSC Mentor/Team Progress Form', default='http://bit.ly/2019WeeklyForms', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_handbook = models.URLField('BioEHSC Handbook', default='https://drive.google.com/drive/folders/1XlELltEUiAxq3jSShb3MC5C5792RnTg-', help_text='Check with BioEHSC External Relations/Junior Chair/Senior Chair for if this needs to be updated')
    bioehsc_handbook_feedback_form = models.URLField('BioEHSC Handbook Feedback Form', default='http://bit.ly/2021HandbookFeedbackForm', help_text='Check with BioEHSC External Relations/Junior Chair/Senior Chair for if this needs to be updated')
    bioehsc_video_abstract_example_videos = models.URLField('BioEHSC Video Abstract Examples', default='https://drive.google.com/drive/folders/187VRSJGoOPPYrBFnZ3-_36fxmOWcXYYa?usp=sharing', help_text='Check with BioEHSC External Relations/Junior Chair/Senior Chair for if this needs to be updated')
    bioehsc_resources_drive = models.URLField('BioEHSC Resources Drive',default='https://drive.google.com/drive/folders/1TUWwbkHCH69UbPqiSg82V75H4xd0YyHI?usp=sharing', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_poster_examples = models.URLField('BioEHSC Poster Examples',default='https://drive.google.com/drive/folders/1scVsDs8-UHZ0A_-F7cyYcxtlUIsHFQwP?usp=sharing', help_text='Check with BioEHSC External Relations/Junior Chair/Senior Chair for if this needs to be updated')
    bioehsc_online_application = models.URLField('BioEHSC Application', default='https://bit.ly/2022BioEHSCApplication ', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_petition_form = models.URLField('BioEHSC Petition Form', default='https://bit.ly/2022BioEHSCPetition', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_liability_form = models.URLField('BioEHSC Liability Waiver', default='https://bit.ly/2022BioEHSCLiability', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_photo_release_form = models.URLField('BioEHSC Photo Release Form', default='https://bit.ly/2022BioEHSCPhotoRelease', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_parent_release_form = models.URLField('BioEHSC Parent Release Form', default= 'https://bit.ly/2022BioEHSCParentRelease', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_medical_auth_form = models.URLField('BioEHSC Medical Treatment Authorization Form', default='https://drive.google.com/file/d/1MP60iwxeJtzkdVLr-jXYIiYXeqSb4c5m/view', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_school_auth_form = models.URLField('BioEHSC School Authorization Form', default='https://bit.ly/2022BioEHSCSchoolAuth', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_student_registration_form = models.URLField('BioEHSC Student Registration Form', default='https://www.eventbrite.com/e/2022-bioehsctm-a-bioengineering-high-school-competition-tickets-242124660377', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_fee_waiver = models.URLField('BioEHSC Fee Waiver Form', default='https://forms.gle/6D2ZNDKvCGDfRFzy8', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_paperwork_documentation = models.URLField('BioEHSC Paperwork Documentation', default='https://drive.google.com/drive/folders/1yUP3MriPFu-jGxwegDQjIyiAk8-vmCBt?usp=sharing')
    bioehsc_non_student_registration_form = models.URLField('BioEHSC Visitor (Non-Student) Registration Form', default='http://bit.ly/2018BioEHSC_parent-coach_registration', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_poster_link = models.URLField('BioEHSC Poster Advertisement', default='https://drive.google.com/file/d/1UkgswaV25PVEWn-2xvtvKl53YWeTE4al/view?usp=sharing', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_faculty_volunteer = models.URLField('BioEHSC Faculty Volunteer Signup', default='http://bit.ly/2019BioEHSCFaculty', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_grad_volunteer = models.URLField('BioEHSC Grad Student/Postdoc Volunteer Signup', default='http://bit.ly/2019BioEHSCGradForm', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_industry_volunteer = models.URLField('BioEHSC Industry Volunteer Signup', default='http://bit.ly/2019BioEHSCIndustry', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_ugrad_volunteer = models.URLField('BioEHSC Undergrad Volunteer Signup', default='http://bit.ly/2019BioEHSCVolunteer', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_volunteer_flyer = models.ImageField('BioEHSC Volunteer Flyer', default='BioE-Day-Flyer-Fall-2018.jpg', upload_to='', help_text='TO BE UPDATED EACH SPRING')
    bioe_day_rsvp_form = models.URLField('BioE Day RSVP', default='https://docs.google.com/forms/d/e/1FAIpQLSc_U00mF4xtgj3fhVTvOH2LIjijb6s66frEUvQ1zlDPxCsA1A/viewform', help_text='TO BE UPDATED EACH SPRING')
    bioehsc_ugrad_mentor = models.URLField('BioEHSC Undergraduate Mentorship Form', default='bit.ly/2020MentorRegistration', help_text='TO BE UPDATED EACH SPRING')
    bioe_day_flyer = models.ImageField('BioE Day Flyer', default='BioE-Day-Flyer-Fall-2018.jpg', upload_to='', help_text='TO BE UPDATED EACH SPRING')
    beacon_alum_registration = models.URLField('BEACON 2.0 Alumni Mentor Registration', default='https://docs.google.com/forms/d/e/1FAIpQLSeAPkgZrGG2sjGNPn69yvydIr3_Ylv3OslriX7BCuPsdt5Qwg/viewform', help_text='Check with President if this needs updating')
    bioehsc_hs_flyer = models.ImageField('BioEHSC High School Recruitment Flyer', default='2022_BioEHSC_HS_Flyer_1.jpg', upload_to='', help_text='TO BE UPDATED EACH SPRING')
    def __str__(self):
        return "Links, Forms, Flyers, & Info to Update"
