from fastapi import APIRouter, HTTPException
from app.product.dao import ModelsDAO
from app.product.schemas import SModels_product

router = APIRouter(
    prefix="/product",
    tags=["Продукты"]
)

@router.get("/range_product")
async def product_in_range(from_id: int, to_id: int):
    product = await ModelsDAO.find_id_range(id_column_name="product_id", from_id=from_id, to_id=to_id)
    if not product:
        raise HTTPException(status_code=404, detail="Число слишком большое")
    return product


@router.get("/{id}")
async def get_product(id: str, name: str = None):  # -> List[SModels_product]
    product = await ModelsDAO.model_one_or_none(product_id=id)
    if product is None:
        raise HTTPException(status_code=404, detail="Такого нет")
    return product


@router.post("/add_model")
async def add_product(product_model: SModels_product):
    existing_product = await ModelsDAO.model_one_or_none(category_id=product_model.category_id, name=product_model.name)
    if existing_product:
        raise HTTPException(status_code=409, detail="Уже добавлен")
    await ModelsDAO.add(category_id=product_model.category_id, name=product_model.name)

@router.get("/search/")
async def search_shops_by_partial_name(name: str):
    product = await ModelsDAO.get_product_by_partial_name(name)
    if not product:
        raise HTTPException(status_code=404, detail="Такого нет")
    return product

@router.delete("/delete_model/{id}")
async def delete_product(id: str):
    await ModelsDAO.delete(product_id=id)
