from flask import render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from controllers.experience_controller import get_all_experience_users, level_up, get_user_level, create_new_table
from controllers.task_controller import create_task, view_task, update_complete_task
from controllers.reward_controller import create_new_reward
from form import LoginForm, RegisterForm, TodoForm

from models import Task, User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard_create'))
        return redirect(url_for('dashboard_create'))

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        create_new_table(new_user)
        create_new_reward(new_user)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/dashboard/create', methods=['GET', 'POST'])
@login_required
def dashboard_create():
    form = TodoForm()

    if form.validate_on_submit():
        create_task(current_user, form.title.data, form.description.data, form.priority.data, form.deadline.data)
        return redirect(url_for('dashboard_list'))

    return render_template('/dashboard/create.html', form=form, level=get_user_level(current_user))

@app.route('/dashboard/list')
@login_required
def dashboard_list():
    tasks = view_task(author=current_user, completed='0')
    level_up(current_user)

    if request.args.get('complete') == '1':
        update_complete_task()
        return redirect(url_for('dashboard_list'))

    return render_template('/dashboard/list.html', tasks=tasks, level=get_user_level(current_user))

@app.route('/dashboard/complete')
@login_required
def dashboard_complete():
    tasks = Task.query.filter_by(completed='1', user_id=current_user.id).order_by(Task.priority.desc()).all()

    if (request.args.get('delete') == '1'):
        Task.query.filter_by(id=int(request.args.get('id'))).delete()
        db.session.commit()
        return redirect(url_for('dashboard_complete'))

    return render_template('/dashboard/complete.html', tasks=tasks, level=get_user_level(current_user))

@app.route('/dashboard/hiscore')
@login_required
def dashboard_hiscore():
    experience = get_all_experience_users()
    return render_template('/dashboard/hiscore.html', users=experience, level=get_user_level(current_user))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))