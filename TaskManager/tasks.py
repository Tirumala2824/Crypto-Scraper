from celery import shared_task
from .models import ScrapingJob
from .utils import CoinMarketCap

@shared_task
def scrape_data(job_id, coins):
    job = ScrapingJob.objects.get(id=job_id)
    cmc = CoinMarketCap()
    result = []
    for coin in coins:
        data = cmc.scrape_coin_data(coin)
        result.append({'coin': coin, 'output': data})
    job.result = result
    job.status = 'COMPLETED'
    job.save()
