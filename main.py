from fastapi import FastAPI
from typing import List

from Validate import add_iphone, get_iphone
from Database import iphone_database

app = FastAPI(
    title='the plan to capture Poland'
)

@app.get('/iphone/{iphone_id}', response_model=List[get_iphone])
def Selected_iPhone(iphone_id: int):
    """Страничка конкретного iphone"""

    return [iphone for iphone in iphone_database if iphone.get('id') == iphone_id] # Выводит информацию из бд, по номеру id

@app.get('/catalog')
def Catalog(limit: int = 1, offset: int = 5):
    """Каталог"""

    return [iphone.get('model') for iphone in iphone_database if (limit <= iphone.get('id') <= offset)]  #Выводит названия моделей, если они входят в диапозон

@app.post('/catalog')
def add_iphone(new_iphone: List[add_iphone]):
    """Функция добавляет новый iphone"""

    iphone_database.extend(new_iphone)
    return {"status": 200, "data": iphone_database[-1]}
