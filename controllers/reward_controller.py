from models import Reward
from app import db

def create_new_reward(current_user):
    create_table = Reward(author = current_user, coins = 0)
    db.session.add(create_table)
    db.session.commit()
