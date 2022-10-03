from fastapi import APIRouter

from app.routers.v1.linea_blanca import router_linea_blanca

router = APIRouter()

router.include_router(
    router_linea_blanca,
    tags=["LINEA BLANCA"],
    prefix="/linea-blanca"
)
