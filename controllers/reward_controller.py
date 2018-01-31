from models import Reward
from app import db
from random import random

def create_new_reward(current_user):
    create_table = Reward(author = current_user, coins = 0)
    db.session.add(create_table)
    db.session.commit()

def reward_user(current_user):
    generate_coin = int(random()*100 + 20)
    new_reward = Reward.query.get(current_user.id)
    new_reward.coins += generate_coin
    db.session.add(new_reward)
    db.session.commit()