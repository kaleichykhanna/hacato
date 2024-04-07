from django.db import models
from enum import Enum
from django.core.validators import MaxValueValidator

class Faculty(Enum):
    FCAD = 'Faculty of Computer-Aided Design'
    FITC = 'Faculty of Information Technologies and Control'
    MF = 'Military Faculty'
    FRE = 'Faculty of Radioengineering and Electronics'
    FCSN = 'Faculty of Computer Systems and Networks'
    FIS = 'Faculty of Information Security'
    FEE = 'Faculty of Engineering and Economics'
    TUC = 'Trade Union Committee'  # Профком

class Event(models.Model):
    name = models.TextField(max_length=55) 
    date = models.DateField()
    time = models.TimeField()
    university_building = models.IntegerField(validators=[MaxValueValidator(5)]) 
    description = models.TextField(max_length=1200)
    faculty = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in Faculty])
    date_time_post = models.DateTimeField()
    url = models.TextField()

    def __str__(self):
        return self.name

