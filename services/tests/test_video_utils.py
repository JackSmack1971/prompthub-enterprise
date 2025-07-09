import os
import pytest
from httpx import Response

import services.shared.video_utils as vu

class DummyAsyncClient:
    def __init__(self, status_code: int = 200, json_data: dict | None = None):
        self.status_code = status_code
        self._json = json_data or {}

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def get(self, url: str, headers: dict):
        req = vu.httpx.Request("GET", url, headers=headers)
        return Response(status_code=self.status_code, json=self._json, request=req)

@pytest.mark.asyncio
async def test_fetch_metadata_success(monkeypatch):
    os.environ['VIDEO_API_KEY'] = 'dummy'
    monkeypatch.setattr(vu.httpx, 'AsyncClient', lambda *a, **k: DummyAsyncClient(json_data={"title": "test"}))
    request = vu.VideoRequest(url='https://example.com/video.mp4')
    data = await vu.fetch_metadata(request)
    assert data == {'title': 'test'}

@pytest.mark.asyncio
async def test_fetch_metadata_missing_key(monkeypatch):
    monkeypatch.delenv('VIDEO_API_KEY', raising=False)
    request = vu.VideoRequest(url='https://example.com/video.mp4')
    with pytest.raises(vu.VideoAPIError):
        await vu.fetch_metadata(request)
