from flask import Flask
import json
from data  import catalog

app = Flask(__name__)


@app.get("/")
def home():
    return "Hello from server"


@app.get("/test")
def test():
    return "This is another page"

@app.get ('/api/products')
def get_products ():
    
    return json. dumps (catalog)


app.run(debug=True)


# methods on hhtp requests