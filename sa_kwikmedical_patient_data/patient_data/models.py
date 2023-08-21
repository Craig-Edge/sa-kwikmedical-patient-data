from django.db import models
from django.utils import timezone

class Patient(models.Model):
     
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    nhs_number = models.CharField(max_length=50, null=True, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class PatientCallOut(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('in transit', 'In Transit'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
      
    nhs_number = models.CharField(max_length=50, null=True) 
    datetime = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    actions_taken = models.TextField()
    treatment_notes = models.TextField()
    
    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return f"Call Out for {self.nhs_number} at {self.datetime}"