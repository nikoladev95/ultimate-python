import random


class Dice:
    def roll(self):
        dice_roll = (random.randint(1, 6), random.randint(1, 6))
        return dice_roll