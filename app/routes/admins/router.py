from typing import List, Union
from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.main import BaseModel

from app.auth.auth import get_admin, get_current_user
from app.auth.firebase import UserRecord

from app.models import ValueModel
from app.responses import BaseResponse, Success

router = APIRouter(prefix="/api/v1/admins")

DEFAULT_ADMIN_NUMBER = "+4799999999"

ADMIN_NUMBERS = [
    "+4795415454",
    "+4799999999",
]

IsAdminValueModel = ValueModel.new(isadmin=(bool, False))

AdminsValueModel = ValueModel.new(admins=(List[str], ...))


class ListStringResponse(BaseResponse):
    data: AdminsValueModel


class AdminsOrBoolResponse(BaseResponse):
    data: Union[AdminsValueModel, IsAdminValueModel]


@router.get(
    "/",
    response_model=AdminsOrBoolResponse,
)
@router.get(
    "",
    response_model=AdminsOrBoolResponse,
)
async def get_admins(
    user: UserRecord = Depends(get_current_user),
    list: bool = False,
):
    if list and user.phone_number in ADMIN_NUMBERS:
        return AdminsOrBoolResponse(
            data=AdminsValueModel(
                admins=ADMIN_NUMBERS,
            ),
        )

    return AdminsOrBoolResponse(
        data=IsAdminValueModel(
            isadmin=user.phone_number in ADMIN_NUMBERS,
        ),
    )


@router.post("/", dependencies=[Depends(get_admin)])
@router.post("", dependencies=[Depends(get_admin)])
async def add_admin(number: str):

    if number not in ADMIN_NUMBERS:
        ADMIN_NUMBERS.append(number)

    return Success(detail="Admin has been added")
