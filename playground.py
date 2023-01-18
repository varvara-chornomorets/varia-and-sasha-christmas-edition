import time
DELAY = 5
bonus = Bonus()
if time.time() - bonus.start_time > DELAY:
    bonus.drop()
