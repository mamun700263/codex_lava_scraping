from fastapi import APIRouter
import asyncio
from app.runner import run_scraper

router = APIRouter()

@router.post("/run")
async def google_map_scrapper_view(target: str, file_type: str):
    print(target, file_type)
    data = await run_scraper.delay(target, file_type)
    return {"status": "success","data":data}
