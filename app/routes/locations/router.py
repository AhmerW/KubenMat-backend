from typing import List, Optional

from fastapi import APIRouter, Depends


from app.models import LocationModel
from app.routes.locations.models import (
    LocationValueModel,
    LocationsResponse,
    LocationsValueModel,
)
from app.services.location_service import locationService
from app.auth.auth import get_admin

router = APIRouter(prefix="/api/v1/locations")


@router.get("/", response_model=LocationsResponse)
@router.get("/{id}", response_model=LocationsResponse)
async def get_locations(location_id: Optional[str] = None):
    locations = locationService.get_locations(location_id=location_id)
    return LocationsResponse(
        data=LocationsValueModel(
            locations=locations,
        ),
    )


@router.post("/", response_model=LocationsResponse)
async def add_location(
    location: LocationModel,
    # user: Depends(get_admin),
):
    locationService.add_location(location=location)
    return LocationsResponse(
        data=LocationValueModel(location=location),
    )
