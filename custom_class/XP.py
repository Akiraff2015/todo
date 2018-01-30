from random import random
from math import fabs

from models.experience import Experience

from models.experience_table import ExperienceTable
from app import db

class XP:
    def __init__(self, username=None):
        self.username = username
        self.rand_number = round(random()*100, 1)

    def get_xp_table(self):
        get_xp_table = ExperienceTable.query.get(self.get_level())
        return get_xp_table.xp

    def get_remainder_xp(self):
        return round(fabs(self.get_xp_table() - self.get_xp()), 1)

    def is_level_up(self):
        if self.get_xp() >= self.get_xp_table():
            return True
        return False

    def get_level(self):
        get_lvl = Experience.query.get(self.username.id)
        return get_lvl.level

    def get_xp(self):
        get_xp = Experience.query.get(self.username.id)
        return get_xp.xp

    def level_up(self):
        update_xp = Experience.query.get(self.username.id)
        update_xp.xp = self.get_remainder_xp()
        update_xp.level += 1
        db.session.commit()
        print("[CONSOLE]: Level up!")

    def generate_randxp(self):
        return self.rand_number

    def generate_complete_xp(self):
        new_rand = (self.rand_number / 2)
        return new_rand