from fastapi import APIRouter

router_linea_blanca = APIRouter()

@router_linea_blanca.get("/")
async def get_all_products():
    """
    Get all products to register
    """
    return {"Product": "all"}
