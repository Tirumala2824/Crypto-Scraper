from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import ScrapingJob

class ScrapingJobTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_start_scraping(self):
        url = reverse('start_scraping')
        data = {'coins': ['bitcoin', 'ethereum']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertTrue('job_id' in response.data)

    def test_scraping_status(self):
        job = ScrapingJob.objects.create()
        url = reverse('scraping_status', kwargs={'job_id': str(job.id)})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_job_id(self):
        url = reverse('scraping_status', kwargs={'job_id': 'invalid_id'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
