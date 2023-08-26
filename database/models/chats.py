from app import db
import pytz 

class ChatsModel(db.Model):

    """
    primary key: id
    other fields: user_id, msg_from, message, creation_time
    """

    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer)
    msg_from = db.Column(db.String(100))
    message = db.Column(db.String(5000))
    creation_time = db.Column(db.DateTime)

    def json(self):
        return {'id': self.id, 'user_id': self.user_id, 'msg_from': self.msg_from, 'message': self.message, 'creation_time': self.creation_time}

