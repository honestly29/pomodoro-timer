import time
import threading


def start_timer(duration):
    print(f"Starting timer for {duration // 60} minutes.")
    countdown(duration)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)  # div mod gives you the quotient, remainder 

        # : = start of the format code.
        # 0 = the number should be zero-padded 
        # 2 = the number should be at least 2 digits wide.
        # d = "decimal integer".
        timer = '{:02d}:{:02d}'.format(mins, secs)

        print(timer, end="\r") # overwrites current line with printed value rather than go to the next line
        time.sleep(1)
        t -= 1
    print('Timer finished!')


def pomodoro_cycle(work_duration, short_break, long_break, cycles):
    for i in range(cycles):
        start_timer(work_duration)
        print("Take a short break.")
        start_timer(short_break)

    print("Time for a long break!")
    start_timer(long_break)


def main():
    work_duration = 25 #* 60
    short_break = 5 #* 60
    long_break = 15 #* 60
    cycles = 4

    pomodoro_cycle(work_duration, short_break, long_break, cycles)


if __name__ == "__main__":
    main()