from fastapi import APIRouter

router_jugueteria = APIRouter()

@router_jugueteria.get("/")
async def get_all_products():
    """
    Get all products to register
    """
    return {"hot-wheels": "Mattel",
            "uno": "Mattel",
            "monopoly": "Hasbro",
            "nerf": "Hasbro"}