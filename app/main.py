from app.globals import app

from app.routes.orders.router import router as order_router
from app.routes.admins.router import router as admin_router
from app.routes.locations.router import router as location_router

from app.data import database

app.add_event_handler("startup", database.connect_db)
app.add_event_handler("shutdown", database.close_db)

app.include_router(order_router)
app.include_router(admin_router)
app.include_router(location_router)
