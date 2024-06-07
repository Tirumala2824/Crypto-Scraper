# Crypto-Scraper
This Django project is designed to scrape data from CoinMarketCap using Django REST Framework, Celery, and Selenium.


## Installation

1. **Install the required libraries**:
   ```bash
   pip install django djangorestframework celery requests selenium
   ```

2. **Create a new Django project**:
   ```bash
   django-admin startproject crypto_scraper
   cd crypto_scraper
   ```

3. **Create a new Django app**:
   ```bash
   python manage.py startapp taskmanager
   ```

4. **Set up Celery**:
   - Install Redis (used as the message broker).
   - Update `crypto_scraper/settings.py` to configure Celery.

## Usage

1. **Run Django migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Run the Django application**:
   ```bash
   python manage.py runserver
   ```

3. **Start the Celery worker**:
   ```bash
   celery -A crypto_scraper worker --loglevel=info
   ```

## API Endpoints

- `/api/taskmanager/start_scraping/`: Start a scraping job.
- `/api/taskmanager/scraping_status/<job_id>/`: Get the status of a scraping job.

## Note

Adjust the extraction code in `taskmanager/utils.py` based on the actual HTML structure of the CoinMarketCap pages.

This README provides a brief overview of the project setup and usage, along with important commands for installation and execution. Adjustments may be required based on your specific environment and requirements.
```
