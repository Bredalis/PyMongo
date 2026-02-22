
from crud import Crud

URI = "YOUR_MONGODB_URL"
crud = Crud(URI)

document_id = "6532537798c4f4853acfafe2"

new_data = {
    "name": "Juan",
    "gender": "Male",
    "grade": 9,
}

modified = crud.update(document_id, new_data)
print("Modified documents:", modified)

crud.close_connection()
