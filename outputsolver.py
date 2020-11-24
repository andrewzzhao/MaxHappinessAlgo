import random
"""
x_4 = random.uniform(0, 69.69)
x_5 = random.uniform(0, 69.69 - x_4)
x_7 = 69.69 - x_4 - x_5

x_4 + x_5 + x_7 = 69.69

x_8 + x_9 = 72.69
x_6 + x_0 + x_1 = 89.69
x_2 + x_3 = 43.11


y_4 + y_5 + y_7 <= 157.69/4
y_8 + y_9 <= 157.69/4
y_6 + y_0 + y_1 <= 157.69/4
y_2 + y_3 <= 157.69/4
"""

numRooms = 4
numPeople = 10

inputs = [[-1 for _ in range(numPeople)] for _ in range(numPeople)]

sums = [random.uniform(30, 250) for _ in range(numRooms)]

constraints = [random.uniform(40, 200) for _ in range(numRooms)]




