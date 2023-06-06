##Question1
def getTranspose(matrix):
 result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
 return result


def multiplyMatrices(matrixA, matrixB):
 result = [[0 for x in range(len(matrixA[0]))] for y in range(len(matrixB))]
 for i in range(len(matrixA)):
  for j in range(len(matrixB[0])):
   for k in range(len(matrixB)):
    result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result


def matrixPower(matrix, power):
 for i in range(power - 1): matrix = multiplyMatrices(matrix, matrix)
 return matrix


def matrixAddition(matrixA, matrixB):
 if len(matrixA) != len(matrixB) or len(matrixA[0]) != len(matrixB[0]):
  return None
  else:
  result = [[matrixA[i][j] + matrixB[i][j]
             for j in range(len(matrixA[0]))]
            for i inrange(len(matrixA))]
 return result
 a = [[1, 2, 3, 1]]
 b = [[1], [1], [5]]
 A = [[1, 3, 5], [2, 4, 6], [7, 9, 11]]
 B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
 first = multiplyMatrices(a, getTranspose(a))
 second = matrixAddition(b, getTranspose(a))
 third = multiplyMatrices(A, getTranspose(A))
 fourth = matrixPower(A, 3)
 fifth = multiplyMatrices(A, B)
 print(first, "\n")
 print(second, "\n")
 print(third, "\n")
 print(fourth, "\n")
 print(fifth)


###Question_2
import numpy as np
A=np.zeros([10,5],dtype=int)

B=np.ones([5,10],dtype=int)
print("Matrix-A:\n",A)
print("\nMatrix-B:\n",B)

AB_Multiplication=np.dot(A,B)
print("\nResultant matrix:\n")
print(AB_Multiplication)
###Question_3
import numpy as np

 p = np.tile(y,3)
 q = np.vstack(p,p)
 r = np.hstak(x,q)
 s = np.transpose(z)
 t = np.vstack(s,p)
 u = np.hstack(z,t)
 m = np.vstack(r,u)


##Question4
import numpy as np
x = np.arange(12.0)
x1 = np.reshape(2,2,3) x2 = np.reshape(2,3,2)
X_multiplication = np.matmul (x1,x2)
##Question5
import numpy as np
M_diagonal = np.diag(m)

