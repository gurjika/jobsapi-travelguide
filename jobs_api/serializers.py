from rest_framework import serializers

from jobs_api.models import Company, Job
from django.contrib.auth import get_user_model

User = get_user_model()


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['first_name', 'last_name']
        model = User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'description', 'number_of_employees', 'image']
        model = Company

    def create(self, validated_data):
        return Company.objects.create(created_by=self.context['user'], **validated_data)


class JobSerializer(serializers.ModelSerializer):
    created_by = SimpleUserSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        fields = ['title', 'description', 'location', 
                  'company', 'employment_type', 
                  'application_deadline', 'salary', 'requirements','responsibilities', 'created_by', 'company_id']
        model = Job



    