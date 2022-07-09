from typing import Final, List, Dict, Optional
import secrets
import asyncio

from fastapi import WebSocket


def _generate_client_id() -> str:
    return secrets.token_hex(3)


class WsClient:
    def __init__(self, ws: WebSocket) -> None:
        self._clients.append(ws)
        self._queue = asyncio.Queue()
        self._id = _generate_client_id()

    @property
    def queue(self) -> asyncio.Queue:
        return self._queue

    @property
    def id(self) -> str:
        return self._id


class WsService:
    def __init__(self) -> None:
        self._clients: List[WsClient] = list()

    def add_client(self, client: WsClient) -> None:
        self._clients.append(client)

    def add_ws(self, ws: WebSocket) -> WsClient:
        client = WsClient(ws)
        self.add_client(client)

        return client

    def send_json(self, data: Dict, client_id: Optional[str] = None) -> None:
        for client in self._clients:
            if client_id and client.id != client_id:
                continue

            client.queue.put_nowait(data)


wsService: Final[WsService] = WsService()
