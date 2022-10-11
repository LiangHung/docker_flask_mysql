from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField
from wtforms.fields.html5 import EmailField
from model import Users

from wtforms.validators import ValidationError
from wtforms import BooleanField
class FormRegister(Form):

    """依照Model來建置相對應的Form

    password2: 用來確認兩次的密碼輸入相同
    """
    username = StringField('使用者名稱', validators=[
        validators.DataRequired(),
        validators.Length(6, 15)
    ])
    email = EmailField('信箱', validators=[
        validators.DataRequired(),
        validators.Length(1, 50),
        validators.Email()
    ])
    password = PasswordField('密碼', validators=[
        validators.DataRequired(),
        validators.Length(5, 10),
        validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    ])
    password2 = PasswordField('再次輸入密碼', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('建立新帳戶')

    def validate_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('信箱已被註冊')

    def validate_username(self, field):
        if Users.query.filter_by(username=field.data).first():
            raise  ValidationError('使用者名稱已被註冊')


class FormLogin(Form):
    """
    使用者登入使用
    以email為主要登入帳號，密碼需做解碼驗證
    記住我的部份透過flask-login來實現
    """

    email = EmailField('信箱', validators=[
        validators.DataRequired(),
        validators.Length(5, 30),
        validators.Email()
    ])

    password = PasswordField('密碼', validators=[
        validators.DataRequired()
    ])

    remember_me = BooleanField('維持登入狀態')

    submit = SubmitField('登入')


