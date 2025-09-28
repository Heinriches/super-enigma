# You can perform different actions for
# both inner and outer loops.

# The code below prints the day for each iteration
# of the outer loop and then prints all tasks for
# each inner loop iteration:

days = ['Monday', 'Tuesday', 'Wednesday']
tasks = ['Gym', 'Homework', 'Pool']

for day in days:
    print(day + ':')
    for task in tasks:
        print(task)