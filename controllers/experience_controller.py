from flask import render_template
from models.experience import Experience
from models.experience_table import ExperienceTable
from math import fabs
from app import db

def get_all_experience_users():
    xp = Experience.query.order_by(Experience.total_xp.desc()).all()
    return xp

def get_user_level(current_user):
    user = Experience.query.filter_by(author=current_user).first()
    return user.level

def level_up(current_user):
    user_xp = Experience.query.filter_by(author=current_user).first()
    xp_table = ExperienceTable.query.get(user_xp.level)

    # Check if the user is available to level up
    if user_xp.total_xp >= xp_table.xp:
        update = Experience.query.filter_by(author=current_user.i).first()
        remainder = round(fabs(user_xp.total_xp - xp_table.xp), 1)
        update.xp = remainder
        update.level += 1
        db.session.commit()

# Create new row, if is a new user registered
def create_new_table(current_user):
    create_table = Experience(author = current_user, level = 1, xp = 0.0, username = current_user.username, total_xp = 0.0)
    db.session.add(create_table)
    db.session.commit()