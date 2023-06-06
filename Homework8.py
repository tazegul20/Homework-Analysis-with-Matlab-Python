#Question1
import numpy as np

a_arrange = np.arange(0, 11, 1)
print('a_arrange =', a_arrange)

b_arrange = np.arange(7, 19, 2)
print('b_arrange =', b_arrange)

c_arrange = np.arange(0, 2.5, 0.5)
print('c_arrange =', c_arrange)

d_arrange = np.arange(0, -19, -1.5)
print('d_arrange =', d_arrange)


a_linspace = np.linspace(0, 10, 11)
print('a_linspace =', a_linspace)

b_linspace = np.linspace(7, 17, 6)
print('b_linspace =', b_linspace)

c_linspace = np.linspace(0, 2, 5)
print('c_linspace =', c_linspace)

d_linspace = np.linspace(0, -18, 13)
print('d_linspace =', d_linspace)

a_arrange1 = np.arange(0, 5, 1)
a_arrange2 = np.arange(5, 11, 1)
a_r = np.r_['r',a_arrange1,a_arrange2]
print('a_r =', a_r)

b_arrange1 = np.arange(7, 11, 2)
b_arrange2 = np.arange(11, 19, 2)
b_r = np.r_['r',b_arrange1,b_arrange2]
print('b_r =', b_r)

c_arrange1 = np.arange(0, 1, 0.5)
c_arrange2 = np.arange(1, 2.5, 0.5)
c_r = np.r_['r',c_arrange1,c_arrange2]
print('c_r =', c_r)

d_arrange1 = np.arange(0, -10.5, -1.5)
d_arrange2 = np.arange(-10.5, -19, -1.5)
d_r = np.r_['r',d_arrange1,d_arrange2]
print('d_r =', d_r)
##Question2
import numpy as np
np.random.seed(1)
x = np.random.randn(20)
y = np.cumsum(x)
z = np.sum(x)
for i in range(0,len(y)):
    if(np.round(y[i],8)==np.round(z,8)):
        print("{}th element of y is equal to z".format(i))
        break
w = np.diff(np.cumsum(x))
checking = np.array_equal(x,w)
print(checking)

##Question3
import numpy as np

x = [12, 13, 5, 7, 8, 4.5, 6.12, 3, 4, 8, 9, 12.5, 13, 14]
maximum_value = np.max(x)
minimum_value = np.min(x)
mean_value = np.mean(x)
median_value = np.median(x)
variance = np.var(x)
first_quartile = np.quantile(x, 0.25)
third_quartile = np.quantile(x, 0.75)
interquartile = third_quartile - first_quartile

print("Max: ", maximum_value)
print("Min: ", minimum_value)
print("Mean: ", mean_value)
print("Median: ", median_value)
print("Variance: ", variance)
print("First quartile: ", first_quartile)
print("Third quartile: ", third_quartile)
print("Interquartile range: ", interquartile)


y = [np.nan, 2.356, 4, 6, 7.321, np.nan, 3, 8, 9, np.nan, 5, 3.3, 4.5, 7]
maximum_value = np.nanmax(y)
minimum_value = np.nanmin(y)
mean_value = np.nanmean(y)
median_value = np.nanmedian(y)
variance = np.nanvar(y)
first_quartile = np.nanquantile(y, 0.25)
third_quartile = np.nanquantile(y, 0.75)
interquartile = third_quartile - first_quartile

print("Max: ", maximum_value)
print("Min: ", minimum_value)
print("Mean: ", mean_value)
print("Median: ", median_value)
print("Variance: ", variance)
print("First quartile: ", first_quartile)
print("Third quartile: ", third_quartile)
print("Interquartile range: ", interquartile)
##Question4
x=[-10,-4,3,2,1.5,6,8,9,0,11,12,2.5,3.3,7,-4]
question4 = []
for i in x:
    if i > 3 and i <=9:
        question4.append(i)
print(question4)
##Question5
import numpy as np
np.random.seed(0)
x = np.random.randn(15, 30)
question5_a = ((1 < x) & (x <= 2)).sum()
print(f'Number of elements greater than 1 and less than equal to 2 is {question5_a}')

np.random.seed(0)
x = np.random.randn(15,30)
question5_b = x[(0.9 < x) & (x < 1)]
print(question5_b)
