class OrderErrors:
    ORDER_NOT_CREATED = "Bestillingen ble ikke oprettet"
    ORDER_EXCEEDED_LIMIT = "Du har ikke lov å ha mer enn {n} bestillinger om gangen."
    ORDER_NOT_EXISTING = "Bestillingen(e) eksisterer ikke"


class LocationErrors:
    LOCATION_NOT_CREATED = "Lokasjonen ble ikke opprettet"
    LOCATION_EXISTING = "Lokasjonen eksisterer allerede"


class Errors:
    Order = OrderErrors()
    Location = LocationErrors()
