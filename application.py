from fastapi import FastAPI
from typing import List

from app.Validate import add_iphone, get_iphone, update_iphone, patch_iphone
from app.Database import iphone_database

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

@app.post('/add_iphone')
def add_iphone(new_iphone: List[add_iphone]):
    """Функция добавляет новый iphone"""

    iphone_database.extend(new_iphone)
    return {"status": 200, "data": iphone_database[-1]}

@app.put('/update_iphone')
def update_iPhone(put_iphone: List[update_iphone]):
    """Функция обновляет всю информацию про модель в базе данных"""

    for iphone in iphone_database:
        if iphone.get('id') == put_iphone[0].id:
            iphone_database[(put_iphone[0].id - 1)] = put_iphone[0]
            return iphone_database

@app.delete("/iphone/{iphone_id}")
def delete_iPhone(iphone_id: int):
    """Функция удаляет iphone по id"""

    for iphone in iphone_database:
        if iphone.get('id') == iphone_id:
            iphone_database.remove(iphone)
            return iphone_database

@app.patch('/iphone/{iphone_id}')
def patch_price(iphone_id: int, price: List[patch_iphone]):
    """Функция меняет цену в базе данных, если поступила новая цена (если поступил 0, цена не будет меняться)"""

    for iphone in iphone_database:
        if iphone.get('id') == iphone_id:
            iphone["DNS"] = price[0].DNS if price[0].DNS != 0 else iphone["DNS"]
            iphone["Mvideo"] = price[0].Mvideo if price[0].Mvideo != 0 else iphone["Mvideo"]
            iphone["Eldorado"] = price[0].Eldorado if price[0].Eldorado != 0 else iphone["Eldorado"]
            iphone["MTS"] = price[0].MTS if price[0].MTS != 0 else iphone["MTS"]
            return iphone_database





