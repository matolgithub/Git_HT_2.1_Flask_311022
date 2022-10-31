from flask import Flask, render_template, request
from flask import jsonify

from views import AdView

app = Flask("app")


@app.route("/")
@app.route("/index/")
def index_page():
    return render_template("index.html", title="Index_Title",
                           text="Main page of the website!", main_string="--Flask - it is very COOL!--")


app.add_url_rule("/ads/<int:id_ad>/", view_func=AdView.as_view("ads_delete"), methods=["DELETE", "GET"])
app.add_url_rule("/ads", view_func=AdView.as_view("ads_create"), methods=["POST"])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
