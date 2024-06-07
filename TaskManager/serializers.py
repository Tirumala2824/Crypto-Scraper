from rest_framework import serializers
from .models import ScrapingJob

class ScrapingJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapingJob
        fields = ['id', 'created_at', 'updated_at', 'status', 'result']
