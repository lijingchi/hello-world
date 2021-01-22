# Introdction to python
# power
print(2 ** 6)

# type function
a = False
type(a)

# [start : end], start inclusive, end not inclusive
list1 = ["a", "b", "c", "d"]
print(list1[1:3])

# delete elements in a list del()
del(list1[0])
print(list1)

# copy the list
y = list1 # list1 change with y
z1 = list(list1)
z2 = list1[:]

# sorted(list, reverse = )
sorted(list1, reverse = True)

# import package     not recommend  package.function()
# import package as pk    pk.function()
# from package import function      function()
import numpy as np
print(np.pi)

# matplotlib
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.5, 3.5, 5.3, 6.9]
plt.plot(year, pop)
plt.show() 
plt.scatter(year, pop)
# plt.xscale("log")
plt.show() 

# plt.xlabel("") plt.ylabel("") plt.title("")
# plt.yticks()

# Scatter plot
# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
# plt.xscale('log') 
# plt.xlabel('GDP per Capita [in USD]')
# plt.ylabel('Life Expectancy [in years]')
# plt.title('World Development in 2007')
# plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# # Additional customizations
# plt.text(1550, 71, 'India')
# plt.text(5700, 80, 'China')

# # Add grid() call
# plt.grid(True)

# # Show the plot
# plt.show()

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe["norway"])


# pandas

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,"drives_right"])

# Print out drives_right column as DataFrame
print(cars.loc[:,["drives_right"]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,["cars_per_cap", "drives_right"]])

# enumerate
seasons = ['Spring', 'Summer', 'Fall', 'Winter']

print(list(enumerate(seasons)))

print(list(enumerate(seasons, start=1)))       # 下标从 1 开始

# for loop in dictionary
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# for loop in numpy array
# Iterate over europe
for k, v in europe.items():
    print("the capital of " + k + " is " + v)

# Import numpy as np
import numpy as np

# For loop over np_height
for i in np_height:
    print(str(i) + " inches")

# For loop over np_baseball
for i in np.nditer(np_baseball):
    print(i)

# for loop in pandas DataFrame
