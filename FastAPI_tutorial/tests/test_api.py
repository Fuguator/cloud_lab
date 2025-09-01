import pytest
from httpx import AsyncClient, ASGITransport
from test_tutorial import app

@pytest.mark.asyncio
async def test_get_books():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as async_client:
        response = await async_client.get("/books")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2


@pytest.mark.asyncio
async def test_post_books():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as async_client:
        response = await async_client.post("/books", json={
            "title": "New Book",
            "author": "Author Name"
        })
        assert response.status_code == 200
        data = response.json()
        assert data == {"success": True, "message": "Книга добавлена"}