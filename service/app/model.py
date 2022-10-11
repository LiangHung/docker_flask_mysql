from app import db
from flask_login import UserMixin
from app import login_manager



class Users(db.Model, UserMixin):
    """記錄使用者資料的資料表"""
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'username:%s, email:%s' % (self.username, self.email)






#db.create_all()