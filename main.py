from flask import Flask, render_template, request
from flask import jsonify

app = Flask("app")


@app.route("/")
@app.route("/index/")
def index_page():
    return render_template("index.html", title="Index_Title",
                           text="Main page of the website!", main_string="--Flask - it is very COOL!--")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
