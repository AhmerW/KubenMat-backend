from abc import ABC

from app.data.database import Database


class BaseCollectionService(ABC):
    __slots__ = ("_client", "_collection")

    async def __aenter__(
        self,
    ) -> "BaseCollectionService":
        self._client = Database.client
        return self

    async def __aexit__(self, *_, **__) -> None:
        ...
