from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import login_user, current_user, login_required, LoginManager, logout_user
import os
from knapsack01_solver import knapsack01


#  取得啟動文件資料夾路徑
pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#  新版本的部份預設為none，會有異常，再設置True即可。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#  設置資料庫為mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:root@mysql:3306/user'
app.config['SECRET_KEY']='your key'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
SESSION_PROTECTION = 'strong'

@login_manager.user_loader
def load_user(user_id):
    from model import Users
    return Users.query.get(user_id)

# create the DB on demand
@app.before_first_request
def create_tables():
    db.create_all()

# registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    from form import FormRegister
    from model import Users
    form = FormRegister()
    if form.validate_on_submit():
        user = Users(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('註冊成功')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/success')
def succ():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home', methods=['POST'])
def home_post():
    coupon = request.values['coupon']
    items_amount = request.values['item']
    items_name = request.values['name']
    an_item_amount = request.values['amount']
    price = request.values['price']
    res_list, res_name, res = knapsack01(items_amount, coupon, an_item_amount, price, items_name)
    answer = '點'
    for name in res_name:
        answer += name + ','
    answer = answer[0:len(answer)-1]
    answer += '套餐, 可吃到最多份量為'
    answer += str(res)
    answer += '克(g)~'
    your_support = '感謝支持本服務!'
    return render_template('result.html', answer=answer, your_support=your_support)

@app.route('/login', methods=['GET', 'POST'])
def login():
    from form import FormLogin
    from model import Users
    form = FormLogin()
    if form.validate_on_submit():
        #  當使用者按下login之後，先檢核帳號是否存在系統內。
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            #  當使用者存在資料庫內再核對密碼是否正確。
            if form.password.data == user.password:
                #  加入參數『記得我』
                login_user(user, form.remember_me.data)
                #  使用者登入之後，將使用者導回來源url。
                #  利用request來取得參數next
                next = request.args.get('next')
                #  自定義一個驗證的function來確認使用者是否確實有該url的權限
                if not next_is_valid(next):
                    #  如果使用者沒有該url權限，那就reject掉。
                    return 'Bad Boy!!'
                return redirect(next or url_for('home'))
                # return 'Welcome' + current_user.username
            else:
                #  如果密碼驗證錯誤，就顯示錯誤訊息。
                flash('錯誤的信箱或密碼')
        else:
            #  如果資料庫無此帳號，就顯示錯誤訊息。
            flash('錯誤的信箱或密碼')
    return render_template('login.html', form=form)

#  加入function
def next_is_valid(url):
    return True



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Log Out See You.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
