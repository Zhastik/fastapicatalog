from fastapi import FastAPI
from typing import List, Optional

import uvicorn

from app.Validate import add_iphone, get_iphone, update_iphone, patch_iphone
from app.shop.router import router as router_shop
from app.price.router import router as router_price
from app.product.router import router as router_model
from app.categories.router import router as router_category

# from app.Database import iphone_database

app = FastAPI(
    title='the plan to capture Poland'
)

app.include_router(router_model)
app.include_router(router_price)
app.include_router(router_shop)
app.include_router(router_category)
