from src import db


class Logs(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer)
    message = db.Column(db.Text)
    log_type = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
