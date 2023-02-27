from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Semester(models.Model):
    TERMS = (
    ('Spring', 'Spring'),
    ('Fall', 'Fall'),
    )
    term = models.CharField(max_length=6, choices=TERMS)
    year = models.PositiveSmallIntegerField()
    semesters = models.Manager()

    def __str__(self):
        return "{} {}".format(self.term, str(self.year))

class Position(models.Model):
    TITLES = (
    ('Executive Officers', (
        ('PRES', 'President'),
        ('EVP', 'External Vice President'),
        ('IVP', 'Internal Vice President'),
        ('TREAS', 'Treasurer'),
        ('SEC', 'Secretary'),
        ('BIOEHSCSENIOR', 'BioEHSC™ Senior Chair'),
        ('BIOEHSCEXT', 'BioEHSC™ External Relations Chair'))),
    ('Non-Executive Officers', (
        ('PRODEV', 'Professional Development Chair'),
        ('PUBL', 'Publicity Chair'),
        ('ACA', 'Academic Chair'),
        ('HIST', 'Historian'),
        ('HISTCO', 'Co-Historian'),
        ('SOC', 'Social Chair'),
        ('WEBMAS', 'Webmaster'),
        ('PROJ', 'Projects Chair'),
        ('BIOEHSCJUNIOR', 'BioEHSC™ Junior Chair'),
        ('BIOEHSCJRCO', 'BioEHSC™ Junior Co-Chair'),
        ('COMMSERVE', 'Community Service Chair'),
        ('BDB', 'BDB DeCal Facilitator'),
        ('OUTR', 'Outreach Chair'))),
    ('Assistant Officers', (
        ('ASSISACA', 'Academic Assistant Officer'),
        ('ASSISOUTR', 'Outreach Assistant Officer'),
        ('ASSISPRODEV', 'Professional Development Assistant Officer'),
        ('ASSISPROJ', 'Projects Assistant Officer'),
        ('ASSISIVP', 'Internal Vice President Assistant Officer'),
        ('ASSISEVP', 'External Vice President Assistant Officer'),
        ('ASSISBDB', 'BDB DeCal Assistant Facilitator'),
        ('ASSISTREAS', 'Treasurer Assitant Officer'))),
    ('Advisors', (
        ('SRADV', 'Senior Advisor'),
        ('FACADV', 'Faculty Advisor')
        ))
    )
    title = models.CharField(max_length=50, choices=TITLES)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='positions')
    positions = models.Manager()

    def rank(self):
        cache = dict(Position.TITLES)
        for (k, v) in cache.items():
            if (self.title, self.get_title_display()) in cache[k]:
                return k
        return None

    def __str__(self):
        return "{}: {}".format(self.title, str(self.semester))


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Officer/Candidate User Profiles'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_officer = models.BooleanField('Officer Status', default=False)
    is_candidate = models.BooleanField('Candidate Status', default=False)
    is_beacon_alumnus = models.BooleanField('BEACON 2.0 Alumnus', default=False)
    alumnus_last_contacted = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, help_text="Last contacted date, need to manually")
    linkedin = models.URLField("LinkedIn Profile", blank=True)
    beacon_bio = models.TextField("Bio for Alumni (BEACON 2.0)", blank=True, help_text="Ex: BioE major, EECS minor, \
    former BioEHS [position] in [semester, year], part of [professor name & research area] lab. \
    Currently working at _______. Feel free to contact me or add me on LinkedIn.")
    userprofiles = models.Manager()
    if is_officer:
        positions = models.ManyToManyField(Position, related_name='officers', blank=True)
        image = ProcessedImageField(upload_to='headshots/', default='headshots/default.jpg',
                                               processors=[ResizeToFill(200, 300)],
                                               options={'quality': 2000},
                                               format='JPEG')
    if is_candidate:
        waiver_submission = models.BooleanField('Waiver Submission', default=False, blank=True)
        dues_1 = models.BooleanField('Membership Dues Part 1', default=False, blank=True)
        dues_2 = models.BooleanField('Membership Dues Part 2', default=False, blank=True)
        photoshoot = models.BooleanField('Photoshoot', default=False, blank=True)
        #resume_workshop = models.BooleanField('Résumé Workshop', default=False, blank=True)
        resume_submission = models.BooleanField('Revised Résumé Submission', default=False, blank=True)
        linkedin_workshop = models.BooleanField('LinkedIn Workshop', default=False, blank=True)
        prodev_event = models.BooleanField('Professional Development Event', default=False, blank=True)
        academic_event = models.BooleanField('Academic Event', default=False, blank=True)
        outreach_event = models.BooleanField('Outreach Event', default=False, blank=True)
        project_event = models.BooleanField('Project Event', default=False, blank=True)
        social_event_1 = models.BooleanField('Social Event 1', default=False, blank=True)
        social_event_2 = models.BooleanField('Social Event 2', default=False, blank=True)
        social_event_3 = models.BooleanField('Social Event 3', default=False, blank=True)
        #buddy_hangouts = models.BooleanField('Buddy Hangouts', default=False, blank=True)
        #family_competition = models.BooleanField('Family Competition', default=False, blank=True)
        candidate_challenge = models.BooleanField('Candidate Challenge Night', default=False, blank=True)
        retreat = models.BooleanField('Candidate Retreat', default=False, blank=True)
        ccc = models.BooleanField('Cross Committee Conference', default=False, blank=True)
        gm_1 = models.BooleanField('General Meeting 1', default=False, blank=True)
        gm_2 = models.BooleanField('General Meeting 2', default=False, blank=True)
        gm_3 = models.BooleanField('General Meeting 3', default=False, blank=True)
        banquet = models.BooleanField('End of the Year Banquet', default=False, blank=True)
        officer_challenges = models.BooleanField('Officer Challenges', default=False, blank=True)
        


        notes = models.TextField(blank=True, help_text="Enter any additional admin notes for the user; i.e. 'Academic Event candidate requirement fulfilled on MM/DD/YYYY with a makeup event, marked as completed'")

    def __str__(self):
        return self.user.get_full_name()


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
