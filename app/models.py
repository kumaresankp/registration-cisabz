from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=20, choices=[
        ('technical', 'Technical'),
        ('non_technical', 'Non-Technical'),
    ])

    def __str__(self):
        return self.name

class Registration(models.Model):
    # Fields for the registration form
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=255)
    
    # Many-to-Many relationship with Event
    technical_events = models.ManyToManyField(Event, related_name='technical_registrations', blank=True)
    non_technical_events = models.ManyToManyField(Event, related_name='non_technical_registrations', blank=True)
    
    # Contact information fields
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} ({self.college})'
