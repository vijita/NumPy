import numpy as np

# Commonly used functions

# Create a single dimension array from a known list

List_1 = [1,2,3,4,5,6]
array_1 = np.array(List_1)
print("The one dimensional array is", array_1)
print("The type is", type(array_1))
print("The data type is", array_1.dtype)

array_1 = np.array((List_1),dtype = 'float32')
array_1[1] = 9.0
print("After replacing the second element,",array_1)

# Create a two dimensional array

array_2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
array_2.shape
array_2[1,1]
array_2[0,:]
array_2[1:,1:]
array_2[1,:2]

# Other methods to create arrays

np.zeros((2,2))
np.ones((4,3,2))
np.eye(3,3)
np.linspace(2,20,5)
np.arange(2,20,5)
np.random.rand(4,2)
np.random.randint(0,10,3)

# Common operations
array_3 = np.array([1,3,5])
array_4 = np.array([2,4,6])

array_3 + array_4
array_3 / array_4

c = np.vstack((array_3,array_4))
np.transpose(c)

d = np.hstack((array_3,array_4))
np.sort(d)
np.reshape(d,(3,2))

# Import a csv dataset and run statistical calculations
# Year,Month,Mean Temp (°C),Extr Max Temp (°C),
# Extr Min Temp (°C),Total Rain (mm),Total Snow (cm)

e = np.genfromtxt('en_climate_monthly_Toronto.csv',
                  delimiter =',', skip_header = 1)
print("The shape of Toronto's monthly climate dataset is"
      ,e.shape)

# Find Max, Min, range & std.dev of the monthly mean temp.

print("The maximum monthly mean temperature is",
      np.amax(e[:,2]),"deg.C")
print("The minimum monthly mean temperature is",
      np.amin(e[:,2]),"deg.C")
print("The range is",
      np.ptp(e[:,2]),"deg.C")
print("The standard deviation is",
      round((np.std(e[:,2])),2),"deg.C")

# What was the highest temp in Toronto & when did it occur?

Highest_temp = np.amax(e[:,3])
max_temp = np.where(e[:,3] == Highest_temp)
print("The highest temperature of",Highest_temp,
      "deg.C occurred in (YYYY MM)",e[max_temp,:2])

# What was the lowest temp in Toronto & when did it occur?

Lowest_temp = np.amin(e[:,4])
min_temp = np.where(e[:,4] == Lowest_temp)
np.set_printoptions(suppress = True)
print("The lowest temperature of",Lowest_temp,
      "deg.C occurred in (YYYY MM)",e[min_temp,:2])

# What was the mean rainfall in June?

June_rainfall = np.where(e[:,1] == 6)
June_rainfall
print("The mean rainfall in June is",
      round((np.mean(e[June_rainfall,5])),2),"mm")


# What was the maximum monthly snowfall?

print("The maximum snowfall is", np.amax(e[:,6]), "cm")

# Which months have the best bets to enjoy snow in Toronto?

snowfall_months = np.where(e[:,6] != 0)

hist, bin_edges = np.histogram(e[snowfall_months,1],bins = 12)

print("From 1901 to 2000, the occurance of snow ordered from Jan to Dec is"
      ,'\n', hist)

























