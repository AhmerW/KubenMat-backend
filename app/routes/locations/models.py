from typing import List, Union

from app.responses import BaseResponse
from app.models import LocationModel, OrderModelOut, ValueModel, OrderModel

LocationsValueModel = ValueModel.new(
    locations=(
        List[LocationModel],
        list(),
    ),
)

LocationValueModel = ValueModel.new(location=(LocationModel, ...))


class LocationsResponse(BaseResponse):
    data: Union[LocationValueModel, LocationsValueModel]
