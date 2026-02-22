
from crud import Crud

URI = "YOUR_MONGODB_URL"
crud = Crud(URI)

crud.delete({"name": "Juan"})
crud.close_connection()
