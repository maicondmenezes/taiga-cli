from typing import Any, Optional

import httpx


class TaigaAPI:
    def __init__(self, base_url: str, token: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.client = httpx.Client(timeout=30.0)

    def set_token(self, token: str):
        self.token = token

    def _headers(self) -> dict:
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def get(self, endpoint: str, params: dict = None) -> Any:
        resp = self.client.get(f"{self.base_url}/{endpoint}", headers=self._headers(), params=params)
        resp.raise_for_status()
        return resp.json()

    def post(self, endpoint: str, data: dict) -> Any:
        resp = self.client.post(f"{self.base_url}/{endpoint}", headers=self._headers(), json=data)
        resp.raise_for_status()
        return resp.json()

    def patch(self, endpoint: str, data: dict) -> Any:
        resp = self.client.patch(f"{self.base_url}/{endpoint}", headers=self._headers(), json=data)
        resp.raise_for_status()
        return resp.json()

    def delete(self, endpoint: str) -> int:
        resp = self.client.delete(f"{self.base_url}/{endpoint}", headers=self._headers())
        resp.raise_for_status()
        return resp.status_code
