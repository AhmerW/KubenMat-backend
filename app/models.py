from typing import List, Optional
from pydantic import BaseModel
from pydantic.main import create_model


class ValueModel(BaseModel):
    @classmethod
    def new(cls, **fields) -> "ValueModel":
        return create_model("ValueModel", __base__=cls, **fields)


def modelize_list(model: BaseModel, data: List[dict]) -> List[BaseModel]:
    return [model(**item) for item in data]


# Products


class ProductModel(BaseModel):
    name: str
    price: int


# Location


class LocationModel(BaseModel):
    id: str
    name: str
    description: str
    fee: Optional[int] = 0
    active: Optional[bool] = True


# Orders


class OrderProductModel(ProductModel):
    quantity: int


class OrderModel(BaseModel):
    client_number: str
    location_id: str
    timestamp: int
    info: Optional[str] = None
    coupon: Optional[str] = None
    products: List[OrderProductModel]


class OrderModelOut(OrderModel):
    id: str
