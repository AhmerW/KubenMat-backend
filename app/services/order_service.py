from typing import Optional, List

import secrets

from app.errors import Errors
from app.responses import Error

from app.services.base import BaseCollectionService
from app.data.database import get_collection
from app.models import OrderModel, OrderModelOut
from app.routes.orders.models import OrdersValueModel, OrdersResponse

MAX_ORDER_PER_CLIENT_NUMBER = 2


class OrderService(BaseCollectionService):
    COLLECTION_NAME = "orders"

    async def __aenter__(self) -> "OrderService":
        self._collection = get_collection(OrderService.COLLECTION_NAME)
        return await super().__aenter__()

    def generate_order_id(self) -> str:
        return secrets.token_hex(3)

    async def get_orders(
        self,
        id: Optional[str] = None,
    ) -> List[OrderModel]:

        if id is None:
            orders = await self._collection.find().to_list(None)
        else:
            order = await self._collection.find_one({"id": id})
            orders = [order] if order else []

        print(orders)

        if not orders:
            raise Error(Errors.Order.ORDER_NOT_EXISTING)

        return orders

    async def create_order(
        self,
        order: OrderModel,
    ) -> OrderModelOut:
        if (
            await self._collection.count_documents(
                {"client_number": order.client_number},
                limit=MAX_ORDER_PER_CLIENT_NUMBER,
            )
            >= MAX_ORDER_PER_CLIENT_NUMBER
        ):
            raise Error(
                Errors.Order.ORDER_EXCEEDED_LIMIT.format(
                    n=MAX_ORDER_PER_CLIENT_NUMBER,
                ),
            )

        order_id = self.generate_order_id()
        order_out = OrderModelOut(**order.dict(), id=order_id)

        await self._collection.insert_one(order_out.dict())
        return order_out

    async def delete_all(self, client_number: Optional[str] = None) -> None:
        if client_number:
            await self._collection.delete_many({"client_number": client_number})
        else:
            await self._collection.delete_many({})
