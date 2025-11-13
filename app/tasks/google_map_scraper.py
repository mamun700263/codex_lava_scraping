from app.core import Logger
from app.core.data_exporters import FileSaver
from app.google_map.scraper import scraper
from app.celery import celery_app

logger = Logger.get_logger(__file__,'google_map')
@celery_app.task(bind=True,name="map scraper")
async def run_scraper(self,query: str, file_name: str):
    try:
        logger.info(f"Starting scrape for: {query}")
        data = await scraper(query)
        FileSaver.save(data, f"{file_name}")
        logger.info(f"[SUCCESS] Saved results to {file_name}")
        return data
    except Exception as e:
        self.retry(exc=e, countdown=5, max_retries=3)

