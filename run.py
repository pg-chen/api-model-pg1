# -*- coding: UTF-8 -*-
from app import app

# @app.route("/")
# def index():
#     return "API"

if __name__ == "__main__":
    from waitress import serve
    app.run(host="0.0.0.0", port=3000, debug=True)