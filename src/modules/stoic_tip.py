import random


def get_random_tip(tips):
    random_index = random.randint(0, len(tips.get('tips'))-1)
    return tips[random_index]
