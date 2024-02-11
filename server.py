from flask import Flask
import json
app = Flask(__name__)



@app.get("/")
def home():
    return "Hello from flask"

@app.get("/test")
def test():
    return "this is another page"


@app.get("/api/about")
def about():
    me = {"name": "adrian"}
    return json.dumps(me)


app.run(debug=True)