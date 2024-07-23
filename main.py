import time

# time in minutes
total_time = 60
study_time = 10
break_time = 5

total_interval = study_time + break_time #15

count = total_time

for i in range(study_time+1):

    print("Study time: " + str(total_time-i))
    count -= 1
    #time.sleep(1)


print(count)