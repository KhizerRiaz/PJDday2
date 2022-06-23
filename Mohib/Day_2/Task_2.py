
import sys
from numpy import average
def StandardDeviation(arr):
    sumsquared=0
    mean = average(arr)
    for i in range(len(arr)):
        sumsquared = pow((arr[i]-mean),2)
    return sumsquared/len(x)

# x = []
# inputs = int(input("Enter Number Of Values"))

# for i in range(inputs):
#     val = int(input("Enter Number"))
#     x.append(val)


# print("Standard Deviation = ",)

sys.modules[__name__] = StandardDeviation