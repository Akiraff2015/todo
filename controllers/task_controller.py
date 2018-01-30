from flask import request
from models.task import Task
from models.experience import Experience
from app import db
from custom_class.XP import XP

def create_task(author, title, description, priority, deadline):
        random_number = XP().generate_randxp()
        new_task = Task(author=author, title=title, description=description, priority=priority, completed=0, deadline=deadline, xp=random_number)

        update_xp = Experience.query.filter_by(author=author).first()
        update_xp.xp += random_number
        update_xp.total_xp += random_number
        db.session.add(new_task)
        db.session.commit()

def view_task(author, completed):
    tasks = Task.query.filter_by(author=author, completed=completed).order_by(Task.priority.desc()).all()
    return tasks

def update_complete_task():
    update_task = Task.query.get(int(request.args.get('id')))
    update_task.completed = 1
    db.session.commit()