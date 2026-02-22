
from crud import Crud

crud = Crud("YOUR_MONGODB_URL")

crud.insert_data({
    "name": "Juan",
    "gender": "Male",
    "grade": 8
})

crud.close_connection()
