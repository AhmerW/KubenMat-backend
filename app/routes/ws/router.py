from typing import List, Optional

from fastapi import APIRouter, Depends, WebSocket

from app.auth.auth import get_admin

router = APIRouter(prefix="/api/v1/ws")


@router.get("/")
async def ws_root(
    websocket: WebSocket,
    user: Depends(get_admin),
):
    await websocket.send("Hello World!")
    await websocket.close()


@router.websocket("/")
async def ws_connect(
    websocket: WebSocket,
    token: str,
):
    await websocket.accept()
    await websocket.send_text("Hello World!")
    await websocket.close()
