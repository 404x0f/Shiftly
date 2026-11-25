import httpx

from src.core.settings import settings


class APIClient:
    def __init__(self):
        self.base_url = settings.api_url

    async def registration_user(self, data: dict):
        async with httpx.AsyncClient(
            base_url=self.base_url,
        ) as client:
            response = await client.post('/api/v1/user/registration',
                                         json=data)
            if response.status_code == 422:
                print("Validation error:", response.json())
            response.raise_for_status()

            return response.json()

    async def create_shift(self, data: dict):
        async with httpx.AsyncClient(
            base_url=self.base_url,
        ) as client:
            response = await client.post('/api/v1/shift/create', json=data,)
            response.raise_for_status()

            return response.json()


api_client = APIClient()