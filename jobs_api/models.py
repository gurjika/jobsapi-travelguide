from django.db import models
from django.core.validators import  MinValueValidator


class Company(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    number_of_employees = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    created_by = models.ForeignKey('core.user', on_delete=models.CASCADE, related_name='companies')
    image = models.ImageField(upload_to='company_pics', null=True)

class Job(models.Model):

    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('internship', 'Internship'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_jobs')
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
    application_deadline = models.DateField()
    salary = models.CharField(max_length=255, blank=True, null=True)
    requirements = models.TextField()
    responsibilities = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
