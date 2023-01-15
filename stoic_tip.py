import json
import random

def stoic_tip(tips):
    random_index = random.randint(0, len(tips.get('tips'))-1)
    return tips[random_index]


    