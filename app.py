from flask import Flask, request, url_for
from tasks import add_task

app = Flask(__name__)


@app.route("/")
def index():
    name = request.args.get("name", "World")
    return f"Hello {name}"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    result = add_task.delay(a, b)
    return f"task: <a href='{url_for('get', key=result.id)}'>{result.id}</a>"


@app.route("/get/<string:key>")
def get(key):
    result = add_task.AsyncResult(key)
    if result.status == "SUCCESS":
        return f"result: {result.get()}"
    else:
        return f"status: {result.status}"


if __name__ == "__main__":
    app.run(debug=True)
