import asyncio
import os
from typing import Dict

import httpx
from pydantic import BaseModel, HttpUrl, ValidationError

class VideoRequest(BaseModel):
    url: HttpUrl

class VideoAPIError(Exception):
    """Custom exception for video API errors."""

async def fetch_metadata(request: VideoRequest) -> Dict:
    """Fetch video metadata from external service with retries.

    Args:
        request: Validated video request containing a URL.

    Returns:
        Parsed JSON response from the API.

    Raises:
        VideoAPIError: If the API call fails after retries or API key missing.
    """
    api_key = os.getenv("VIDEO_API_KEY")
    if not api_key:
        raise VideoAPIError("Missing API key")

    url = f"https://example.com/metadata?url={request.url}"
    for attempt in range(3):
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(url, headers={"Authorization": f"Bearer {api_key}"})
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as exc:
            last_exc = exc
            await asyncio.sleep(1)
    raise VideoAPIError("API request failed") from last_exc
