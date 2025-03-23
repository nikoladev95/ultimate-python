#
# from lucky_charm.dice import Dice
#
# dice_roll = Dice()
# print(dice_roll.roll())

from pathlib import Path

path = Path()
for file in path.glob('*.*'):
    print(file)