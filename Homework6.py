# question_1
aim = "We are learning Python for scientific computing"

q1a = print(aim[16:22])
q1b = print(aim[0:5])
q1c = print(aim[0:len(aim):3])
q1d = print(aim[-9:-1:2])
# question_2
import math

r = 3.5

q2a = 4 * math.pi * math.pow(r, 2)
print(q2a)
a = 5
b = 7
q2b = math.sqrt((a * (math.cos(math.radians(1.5 * math.pi)))) + (b * (math.sin(math.radians((5 * math.pi) / 2)))))
print(q2b)
y1 = 3.15
y2 = 5
x1 = 7
x2 = 2.15
q2c = (2 * math.pow((y1 - y2), 3) + math.pow(x1, 2)) / (math.pow(x1, 2) - 2 * (x2 - math.pow(x1, 3)))
print(q2c)

# question_3-4
x = [[10, 7],
     [7, 11]]
y = x
y[1][0] = 0.5
print(x)

# Question_5
myList = [[1, 2], 3, "Hello", "ITU"]
print(myList)
q5a = myList.remove(3)
print(myList)
q5b = myList.append([2.5, 1.3j])
q5b2 = myList.append("ITU")
print(myList)
q5c = myList.reverse()
print(myList)
q5d = myList.count("ITU")


###Question_6
q6a= {"University": "ITU", "gamma": 6, 90: "beta"}
print(q6a["gamma"])
q6b=print(q6a.pop(90))
q6a["gamma"]=0.5
q6c=print(q6a)
q6a.update({"teta":6})
q6d=print(q6a)


