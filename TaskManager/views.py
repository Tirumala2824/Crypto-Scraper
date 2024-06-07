from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScrapingJob
from .serializers import ScrapingJobSerializer
from .tasks import scrape_data

class StartScraping(APIView):
    def post(self, request):
        coins = request.data.get('coins', [])
        job = ScrapingJob.objects.create()
        scrape_data.delay(str(job.id), coins)
        return Response({'job_id': job.id}, status=status.HTTP_202_ACCEPTED)

class ScrapingStatus(APIView):
    def get(self, request, job_id):
        try:
            job = ScrapingJob.objects.get(id=job_id)
        except ScrapingJob.DoesNotExist:
            return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ScrapingJobSerializer(job)
        return Response(serializer.data)
