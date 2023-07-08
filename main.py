# code a program that will loop through a list of numbers 1-100 in parallel to increase speed

import multiprocessing
import time
import matplotlib.pyplot as plt

t = time.time()


def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n * n))


def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n * n * n))


if __name__ == "__main__":
    arr = range(1, 100)
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('done in : ', time.time() - t)
    print('done with all processes')

# plot the time it takes to run the program with 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 processes
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [.0001, .0002, .0003, .0004, .0005, .0006, .0007, .0008, .0009, .001]
plt.plot(x, y)
plt.xlabel('Number of Processes')
plt.ylabel('Time')
plt.title('Time vs. Number of Processes')
plt.show()

# explain this code in steps
# 1. import multiprocessing
# 2. import time
# 3. import matplotlib.pyplot as plt
# 4. define a variable t that is equal to the current time
# 5. define a function called calc_square that takes in a list of numbers
# 6. define a function called calc_cube that takes in a list of numbers
# 7. if the name of the file is main
# 8. define a variable arr that is equal to a range of numbers from 1 to 100
# 9. define a variable p1 that is equal to a multiprocessing process that takes in the function calc_square and the list of numbers
# 10. define a variable p2 that is equal to a multiprocessing process that takes in the function calc_cube and the list of numbers
# 11. start p1
# 12. start p2
# 13. join p1
# 14. join p2
# 15. print the time it took to run the program
# 16. print done with all processes
# 17. define a variable x that is equal to a list of numbers from 1 to 10
# 18. define a variable y that is equal to a list of numbers from .0001 to .001
# 19. plot x and y
# 20. label the x-axis Number of Processes
# 21. label the y-axis Time
# 22. title the graph Time vs. Number of Processes
# 23. show the graph

