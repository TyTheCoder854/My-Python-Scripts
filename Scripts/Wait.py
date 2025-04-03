# Imports the modules
import time
import random
# Use this to change the Min and Max number of the seconds the script waits

minRandomNumber = 1
maxRandomNumber = 5

randtime = random.randint(minRandomNumber,maxRandomNumber)

print(f"Waiting for {randtime} seconds...")
time.sleep(randtime)
print(f"{randtime} seconds have passed!")