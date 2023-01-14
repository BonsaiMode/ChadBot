import json
import random

def stoic_tip():
    tip_file = open("./stoic_tips.json", "r")
    tips = json.load(tip_file)
    print(type(tips))
    random_index = random.randint(0, tips.tips.len)
    return tips['tips'][random_index]


    