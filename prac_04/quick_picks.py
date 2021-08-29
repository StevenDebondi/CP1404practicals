"""Quick pick Lottery Ticket Generator"""

import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_picks = []
    for k in range(NUMBERS_PER_LINE):
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_number in quick_picks:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_picks.append(random_number)
    quick_picks.sort()
    print(quick_picks)
