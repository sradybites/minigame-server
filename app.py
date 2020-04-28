from flask import Flask, request
from db import db

app = Flask(__name__)
db_filename = "BFPDB.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app()
with app.app_context():
    db.create_all()

# add routes and JSON serialization base responses

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
