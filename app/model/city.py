from app import db


class City(db.Model):
    __tablename__ = 'citys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), doc=u'城市名')
