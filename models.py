from app import db

class booking(db.Model):
    table = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    info = db.Column(db.String(255))
    date = db.Column(db.String(255))
    hour_start = db.Column(db.Integer)
    hour_end = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.table)
