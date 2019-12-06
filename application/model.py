from datetime import datetime
from flask_login import UserMixin
from  application import db,login_manager

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Posts(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    year=db.Column(db.Integer,nullable=False)
    country=db.Column(db.String(100),nullable=False)
    performer=db.Column(db.String(1000),nullable=False)
    song=db.Column(db.String(1000), nullable=False)

    user_id= db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ',str(self.id), '\r\n',
            'Year:', self.year, '\r\n',
            'Country:', self.country, '\r\n',
            'Performer:', self.performer,'\r\n',
            'Song', self.song, '\r\n'
        ])

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150),nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ',str(self.id), '\r\n',
            'Email:', self.email, '\r\n',
            'Name:', self.first_name, '',
            self.last_name
        ])

