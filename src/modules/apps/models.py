from src import db


class Apps(db.Model):
    __tablename__ = "apps"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    status = db.Column(db.String(255))
    public_key = db.Column(db.String(255))
    private_key = db.Column(db.String(255))
