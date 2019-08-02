from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/surfers', methods=["GET"])
def all_surfers():
    surfers = [surfer.to_dict() for surfer in Surfer.query.all()]
    return jsonify(surfers)

@app.route("/surfers/<int:id>")
def surfer(id):
    surfer = Surfer.query.get(id)
    return jsonify(surfer.to_dict())

@app.route("/surfer", methods=["POST"])
def create_surfer():
    surfer_info = request.json or request.form
    surfer = Surfer(
        name=surfer_info.get("name"), band_id=surfer_info.get("band")
    )
    db.session.add(surfer)
    db.session.commit()

    return jsonify(surfer.to_dict())

@app.route('/waves')
def all_waves():
    waves = [wave.to_dict() for wave in Wave.query.all()]
    return jsonify(waves)

from models import Surfer, Wave

