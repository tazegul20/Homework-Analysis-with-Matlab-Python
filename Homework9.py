
###Question-1
import numpy as np
m = 6
A = np.zeros((m,m))
print("A is as follows")
for i in  range(0,m):
    res=""
    for j in  range(0,m):
        res+=str(int(A[i][j]))

        res+=''
    print(res)

print('')
A_for=np.zeros((m,m))
for i in range(0,m):
    for j in range(0,m):
        res +=str(int(A_for[i][j]))

        res+=''
    print(res)
print('')

A_while=np.zeros((m,m))

i=0
while(i<m):
    j=0
    while(j<m):
        A_while[i][j]=i+j
        j+=1
    i+=1
print("A_while is as follows:")
i=0
while(i<m):
    j=0
    res=""
    while(j<m):
        res+=str(int(A_while[i][j]))

    res+= ""
    j+=1
    print(res)
    i+=1
print('')
###Question-2
import numpy as np
x = np.arange (15)
print("List X is : ",x)
odd = []
even = []
for i in range(0,15):
    if x[i]%2==0:

        even.append(x[i])

    else:
        odd.append(x[i])

print("\nList odd is : ",odd)
print("\nList even is : ",even)

###Question-3
x = [1, 2, -3, 2.5, 7, 8, 9, -2, -4, -3, 4, 3.14, 5.3, -3.3,8]
newlist_x = [i for i in x if i<0]
print("list comprehension")
print(newlist_x)
newSet_x = {i for i in x if i<0}
print("set comprehension")
print(newSet_x)
newdict_x = {i: i for i in x if abs(i)%2==0}
print("dictionary comprehension")
print(newdict_x)
newtuple_x= tuple((i for i in x if i>0))
print("tuple comprehension")
print(newtuple_x)
###Question-4
def quadratic(a, b, c):
    if b ** 2 >= (4 * a * c):

        d = (b ** 2 - 4 * a * c) ** 0.5
        x1 = (-b - d) / (2 * a)
        x2 = (-b + d) / (2 * a)
        print(f"x = {x1}")
        print(f"x = {x2}")
    else:
        print("Real roots does not exists")


quadratic(a, b, c)

###Question-5
import math

def gauss(x, m, s):

  f = math.sqrt(1/(2*3.14*s*s))*math.exp((-1)*(1/(2*s*s)*((x-m)**2)))

  return f

question5a = print(gauss(0,0,1))
question5b = print(gauss(2,0,1))
question5c= print(gauss(0,2,1))
question5d= print(gauss(0,2,2))
question5e= print(gauss(3,3,3))

###Question-6

import numpy as np
def grade_points(letter):
    listt = []
    numpy_array = np.array(listt)
    if(letter == 'A+'):
        numpy_array=np.append(numpy_array, [4])
        return 4,numpy_array
    elif(letter == 'A'):
        numpy_array=np.append (numpy_array, [4.0])
        return 4.0,numpy_array
    elif(letter == 'A-'):
        numpy_array=np.append (numpy_array, [3.7])
        return 3.7,numpy_array
    elif(letter == 'B+'):
        numpy_array=np.append (numpy_array, [3.3])
        return 3.3,numpy_array
    elif(letter == 'B'):
        numpy_array=np.append (numpy_array, [3.0])
        return 3.0,numpy_array
    elif(letter == 'B-'):
        numpy_array=np.append (numpy_array, [2.7])
        return 2.7,numpy_array
    elif(letter == 'C+'):
        numpy_array=np.append (numpy_array, [2.3])
        return 2.3,numpy_array
    elif(letter=='C'):
        numpy_array=np.append (numpy_array, [2.0])
        return 2.0,numpy_array
    elif(letter == 'C-'):
        numpy_array=np.append (numpy_array, [1.7])
        return 1.7,numpy_array
    elif(letter == 'D+'):
        numpy_array=np.append (numpy_array, [1.3])
        return 1.3,numpy_array
    elif(letter == 'D'):
        numpy_array=np.append (numpy_array, [1.0])
        return 1.0,numpy_array
    elif(letter == 'F'):
        numpy_array=np.append (numpy_array, [0])
        return 0,numpy_array
    else:
        numpy_array=np.append (numpy_array, ["INVALID INPUT"])
        return "INVALID INPUT",numpy_array
    return numpy_array
n=input("enter a letter:  ")
print(grade_points(n))
###Question-7
import numpy as np

def Prime(n):
    if n > 1:


        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                print(n, "is not a prime number")
                break
            else:
                print(n, "is a prime number")
        else:
            print(n, "is not a prime number")
x = np.arange(8)
# TEST CASES
question7_1 = x[0]
Prime(question7_1)
question7_2 = x[1]
Prime(question7_2)
question7_3 = x[2]
Prime(question7_3)
question7_4 = x[3]
Prime(question7_4)
question7_5 = x[4]
Prime(question7_5)
question7_6 = x[5]
Prime(question7_6)
question7_7 = x[6]
Prime(question7_7)
question7_8 = x[7]
Prime(question7_8)