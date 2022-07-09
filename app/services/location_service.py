import os
import json
from typing import Final, List, Optional

from app.models import LocationModel
from app.responses import Error
from app.errors import Errors

FILE_PATH = os.path.join("app", "data", "locations.json")
FILE_KEY = "locations"


class LocationService:
    def __init__(self) -> None:
        self._locations: List[LocationModel] = list()
        self.load_locations()

    def load_locations(self) -> None:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)[FILE_KEY]
            self._locations = [LocationModel(**location) for location in data]

    def save_locations(self) -> None:
        with open(FILE_PATH, "w+") as f:
            json.dump({FILE_KEY: self._locations}, f)

    def get_locations(self, location_id: Optional[str] = None) -> List[LocationModel]:
        if location_id:
            return [
                location for location in self._locations if location.id == location_id
            ]
        return self._locations

    def add_location(self, location: LocationModel) -> None:
        for existing_location in self._locations:
            if (existing_location.id == location.id) or (
                existing_location.name == location.name
            ):
                raise Error(Errors.Location.LOCATION_EXISTING)

        self._locations.append(location)
        self.save_locations()


locationService: Final[LocationService] = LocationService()
