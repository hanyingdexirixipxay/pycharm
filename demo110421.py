import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

demo_text = open('demolist110421.txt',"r").read()
#print(demo_list)

demo_list = demo_text.split(',')
demo_list = [int(i) for i in demo_list]
demo_list_sorted = sorted(demo_list, reverse=False)

print(demo_list)
print(demo_list_sorted)

def Average(lst):
    return sum(lst) / len(lst)

average = Average(demo_list)
print(average)
#or with numpy
print(np.mean(demo_list))

print("Average of the list =", round(average, 2))

list1 = [3,4,8,9,6,10]

#sort() cannot be assigned to another variable like append()
sorted_list = sorted(list1)

list_squared = [i**2 for i in sorted_list]

print(list_squared)

ax = plt.subplot()
plt.plot(demo_list, color='blue', marker='o')
ax.set_xticks(range(len(demo_list)))
plt.title('Test Graph')
plt.xlabel('Random Numbers')
plt.ylabel('Values')
plt.show()

