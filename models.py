from app import db

class Surfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Wave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name}



