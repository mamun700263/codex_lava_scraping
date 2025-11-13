import asyncio
import os
from app.core.data_exporters import FileSaver
from app.google_map.scraper import scraper
from app.celery import celery_app


@celery_app.task(bind=True,name="map scraper")
async def run_scraper(self,query: str, file_name: str):
    try:
        print(f"[INFO] Starting scrape for: {query}")
        data = await scraper(query)
        FileSaver.save(data, f"{file_name}")
        print(f"[SUCCESS] Saved results to {file_name}")
        return data
    except Exception as e:
        self.retry(exc=e, countdown=5, max_retries=3)

