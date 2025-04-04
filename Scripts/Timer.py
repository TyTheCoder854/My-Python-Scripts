import time

user_timer = input("How long would you like  your timer to be? (in seconds)")
user_timer_num = int(user_timer)


while not user_timer_num == -1:
    if user_timer_num == 0:
        print("Times Up!")
        break
    else:
        time.sleep(1)
        print(user_timer_num - 1)
        user_timer_num = user_timer_num - 1
