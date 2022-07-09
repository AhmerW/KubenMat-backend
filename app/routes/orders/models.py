from typing import List, Union

from app.responses import BaseResponse
from app.models import OrderModelOut, ValueModel, OrderModel

OrdersValueModel = ValueModel.new(
    orders=(
        List[OrderModelOut],
        list(),
    ),
)

OrderValueModel = ValueModel.new(order=(OrderModelOut, ...))


class OrdersResponse(BaseResponse):
    data: Union[OrdersValueModel, OrderValueModel]
