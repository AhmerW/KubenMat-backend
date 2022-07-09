import os
import asyncio
import concurrent.futures

import firebase_admin
from firebase_admin import auth

from app.responses import Error


class UserRecord(auth.UserRecord):
    @property
    def admin(self) -> bool:
        return self.phone_number in ["s"]


loop = asyncio.get_event_loop()
executor = concurrent.futures.ThreadPoolExecutor(max_workers=20)


cred = firebase_admin.credentials.Certificate(os.path.join("app", "auth", "firebase.json"))
firebase_app = firebase_admin.initialize_app(cred)


def _get_user_async(uid: str) -> UserRecord:
    """Gets a user from firebase"""
    return auth.get_user(uid, firebase_app)


async def verify_user(token: str) -> UserRecord:
    """Verifies with firebase that the token is real"""
    try:
        decoded = auth.verify_id_token(
            token,
            firebase_app,
        )
        return await loop.run_in_executor(executor, _get_user_async, decoded.get("uid"))

    except Exception as e:
        raise Error(str(e))
