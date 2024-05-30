from fastapi import FastAPI

from app.shop.router import router as router_shop
from app.price.router import router as router_price
from app.product.router import router as router_model
from app.categories.router import router as router_category

app = FastAPI(
    title='the plan to capture Poland'
)

app.include_router(router_model)
app.include_router(router_price)
app.include_router(router_shop)
app.include_router(router_category)
