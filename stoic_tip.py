import json
import random

def stoic_tip():
    tips = json.load(open('./stoic_tips.json', 'r'), encoding='utf-8')
    random_index = random.randint(0, len(tips.get('tips'))-1)
    return tips.get('tips')[random_index]


    