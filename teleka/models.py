from datetime import datetime
from teleka import db


class Sender(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # proxy
    scheme = db.Column(db.String(64), default='socks5')
    hostname = db.Column(db.String(15))
    port = db.Column(db.Integer)
    username = db.Column(db.String(15))
    password = db.Column(db.String(30))

    # клиента
    phone_number = db.Column(db.String(15))
    api_id = db.Column(db.String(9))
    api_hash = db.Column(db.String(33))

    # рассылка
    name = db.Column(db.String(15))
    text = db.Column(db.String(100))
    mailing_list_recipient = db.Column(db.String(1000))
    def __repr__(self):
        return '<User {}>'.format(self.username)
