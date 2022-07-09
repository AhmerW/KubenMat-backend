from typing import List, Optional

from fastapi import APIRouter
from fastapi.param_functions import Depends


from app.auth.auth import get_admin
from app.data.database import Database as db
from app.data.database import get_collection
from app.errors import Errors

from app.models import OrderModel, OrderModelOut, ValueModel, modelize_list
from app.responses import Error
from app.routes.orders.models import OrderValueModel, OrdersValueModel, OrdersResponse
from app.services.order_service import OrderService


router = APIRouter(prefix="/api/v1/orders")


@router.get("/", response_model=OrdersResponse)
@router.get("/{id}", response_model=OrdersResponse)
async def get_orders(
    # user=Depends(get_admin),
    id: Optional[str] = None,
):

    async with OrderService() as service:
        orders = await service.get_orders(id=id)

    return OrdersResponse(
        data=OrdersValueModel(orders=modelize_list(OrderModelOut, orders)),
    )


@router.post(
    "/",
    response_model=OrdersResponse,
)
async def create_order(
    order: OrderModel,
    # user=Depends(get_admin),
):

    async with OrderService() as service:
        order_out = await service.create_order(order=order)

    return OrdersResponse(
        data=OrderValueModel(order=order_out),
    )


@router.delete("/")
@router.delete("/{id}")
async def delete_order(
    id: Optional[str] = None,
    # user=Depends(get_admin),
):

    # delete order
    collection = get_collection("orders")
    await collection.delete_one({"_id": id})

    return id
