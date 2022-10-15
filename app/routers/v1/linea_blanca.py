from fastapi import APIRouter

router_linea_blanca = APIRouter()

@router_linea_blanca.get("/")
async def get_all_products(skip: int = 0, limit: int = 10):
    """
    Get all products to register
    """
    return {"Product": "all"}

@router_linea_blanca.get("/{id}")
async def get_one_product(id: int):
    """
    Get one product
    """

    return {"Product": id}

@router_linea_blanca.post("/")
async def send_data_products(item: int):
    """
    Save products
    """

    return {"Product": item}

@router_linea_blanca.patch("/")
async def update_data_products(item: int):
    """
    Update products
    """

    return {"Product": item}

@router_linea_blanca.put("/")
async def update_data_item_products(item: int):
    """
    Updates item of product
    """

    return {"Product": item}

@router_linea_blanca.delete("/")
async def delete_product(item: int):
    """
    Delete of producto
    """

    return {"Product": item}
