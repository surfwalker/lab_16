from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/surfers')
def all_surfers():
    surfers = [surfer.to_dict() for surfer in Surfer.query.all()]
    return jsonify(surfers)

@app.route('/waves')
def all_waves():
    waves = [wave.to_dict() for wave in Wave.query.all()]
    return jsonify(waves)

from models import Surfer, Wave

