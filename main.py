# Randomly Generate numbers until 69420 is reached game thing lol

# By Torry

import random
import time
import psutil
import os

def find():
    attempt = 0
    answer = int(69420)
    while True:

        cpu_start = psutil.cpu_percent()
        time_start = time.time()
        attempt += 1
        guess = random.randint(0,99999) #changing the range will increase or decrease speed

        if guess == answer:

            time_end = time.time()
            cpu_start = psutil.cpu_percent()
            ram_start = psutil.virtual_memory().percent
            time_end = str(time_end - time_start)
            time_end = time_end.replace(' ', '')[:-3]
            time_end = str(time_end)
            cpu_end = psutil.cpu_percent()
            cpu_percent = str(cpu_end - cpu_start)
            ram_end = psutil.virtual_memory().percent
            ram_percent = (ram_end - ram_start)

            print(guess)
            print('')
            print('69420 found!')
            print('')
            print('Attempts Taken: ' + str(attempt))
            print('Time Taken: ' + str(time_end))
            print('')
            print('CPU Usage: ' + str(cpu_percent))
            print('RAM Usage: ' + str(ram_percent))
            print('Battery Usage: 0.0')
            print('')

            with open("highscore.txt", "r+") as hisc:
                hi = hisc.read()
                if not hi:  # not hi will only be true for strings on an empty string
                    hi = '0'
                if attempt > int(hi):
                    print('Score: ' + str(attempt))
                    print('Highest [+]: ' + str(attempt) + ' [NEW]')
                    hisc.seek(0)
                    hisc.write(str(attempt))
                    hisc.truncate()
                else:
                    print('Score: ' + str(attempt))
                    print("Highest [=]: " + str(hi))

            with open("lowscore.txt", "r+") as hisc:
                hi = hisc.read()
                if not hi:
                    hi = '99999'
                if attempt < int(hi):
                    print('Lowest [+]: ' + str(attempt) + ' [NEW]')
                    print('')
                    hisc.seek(0)
                    hisc.write(str(attempt))
                    hisc.truncate()
                else:
                    print("Lowest [=]: " + str(hi))
                    print('')


            input('Press Enter to try again...')

            find()
            return attempt
            return guess

        else:
            print(guess)

def main():
    print('"69420: The Game" (By Torry!)')
    print('')
    print('Will randomly generate numbers (5-digit) until 69420 is reached!')
    print('')
    input('Enter to start...')
    os.system('clear')
    find()

if __name__ == '__main__':
    main()


