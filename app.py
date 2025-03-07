from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/<item>", methods=['POST'])
def entrypoint_with_item(item: str):
    data: str = request.get_data(as_text=True)
    return f"POST {item} to {data}"
