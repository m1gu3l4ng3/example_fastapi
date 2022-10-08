from fastapi import APIRouter

router_linea_blanca = APIRouter()

@router_linea_blanca.get("/")
async def get_all_products(skip: int = 0, limit: int = 10):
    """
    Get all products to register
    """
    return {"Product": "all"}
