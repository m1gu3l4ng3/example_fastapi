from fastapi import APIRouter

from app.routers.v1.linea_blanca import router_linea_blanca
from app.routers.v1.jugueteria import router_jugueteria

router = APIRouter()

router.include_router(
    router_linea_blanca,
    tags=["LINEA BLANCA"],
    prefix="/linea-blanca"
)
router.include_router(
    router_jugueteria,
    tags=["JUGUETERIA"],
    prefix="/jugueteria"
)
