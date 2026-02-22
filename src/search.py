
from crud import Crud

URI = "YOUR_MONGODB_URL"
crud = Crud(URI)

results = crud.create_query({"name": "Lisa"})

for document in results:
    print(document)

crud.close_connection()
