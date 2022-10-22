from flask import Flask, render_template, redirect, request, abort, url_for, flash
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import PasswordField, TextAreaField, StringField, SubmitField, BooleanField, IntegerField
from flask_login import current_user, LoginManager, login_user, logout_user, login_required
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from data import db_session
from data.user import User

app = Flask(__name__)
db_session.global_init("db/database.sqlite")

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.privileges == 0:
            return render_template("driver.html", title='Водитель')
        elif current_user.privileges == 1:
            return render_template("dispatcher.html", title='Диспетчер')
        elif current_user.privileges == 2:
            return render_template("leader.html", title='Руководитель')
    else:
        return render_template("login.html", title='Авторизация')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")



def main():
    app.run()


if __name__ == '__main__':
    main()