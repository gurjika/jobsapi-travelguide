from rest_framework import serializers

from jobs_api.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'description', 'location', 
                  'company', 'employment_type', 'posted_date', 
                  'application_deadline', 'salary', 'requirements','responsibilities']
        model = Job