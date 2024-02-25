from django.db import models
from django.db.models import Q

# Create your models here.
#Committee Database
class Committee(models.Model):
    committee_logo = models.ImageField(upload_to='logos/',blank=True)
    committee_name = models.CharField(max_length=255)
    committee_head = models.CharField(null=True,max_length=200)
    head_tuf_id = models.CharField(max_length=20, null=True, blank=True, help_text="Roll number of the committee head.")
    committee_members_tuf_id = models.TextField(null=True, blank=True, help_text="Enter comma-separated roll numbers of committee members.")
    committee_members = models.TextField(null=True, blank=True, help_text="Enter comma-separated names of committee members.")
    committee_description = models.TextField()

    def __str__(self):
        return self.committee_name
    
    def get_approved_events_queryset(self):
        return self.event_set.filter(event_status="approved")

    approved_events = property(get_approved_events_queryset)

    def get_rejected_events_queryset(self):
        return self.event_set.filter(event_status="rejected")

    rejected_events = property(get_rejected_events_queryset)

    def get_pending_events_queryset(self):
        return self.event_set.filter(event_status="pending")

    approved_events = property(get_pending_events_queryset)

    
#Student Database
class Student(models.Model):
    student_name = models.CharField(max_length=255)
    tuf_id = models.CharField(max_length=20, unique=True)
    year = models.IntegerField()
    committees = models.ManyToManyField('Committee', related_name='committee_participants', blank=True)
    events_participated = models.ManyToManyField('Event', related_name='event_participants', blank=True)
    def __str__(self):
         return f"{self.student_name} - Year {self.year}"

#Event Database
class Event(models.Model):
    committee = models.ForeignKey('Committee', on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    venue = models.CharField(max_length=255)
    admin_approval = models.BooleanField(default=False)
    supporting_documents = models.FileField(upload_to='event_documents/', null=True, blank=True)    

    def __str__(self):
        return self.event_name
