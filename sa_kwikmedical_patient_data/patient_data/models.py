from django.db import models

class Patient(models.Model):
    
    CONDITION_CHOICES = (
        ('critical', 'Critical'),
        ('serious', 'Serious'),
        ('stable', 'Stable'),
        ('minor', 'Minor'),
    )
    
    INJURY_CHOICES = (
        ('head', 'Head Injury'),
        ('fracture', 'Fracture'),
        ('burn', 'Burn'),
        ('internal', 'Internal Injury'),
        ('superficial', 'Superficial Injury'),
    )      
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    condition_type = models.CharField(max_length=50, choices=CONDITION_CHOICES) 
    injury_type = models.CharField(max_length=50, choices=INJURY_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
