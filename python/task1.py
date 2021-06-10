# Program to multiply two matrices 

# 3x3 matrix
X = [[1,9,3],
    [9 ,5,6],
    [7 ,2,9]]
# 3x3 matrix
Y = [[5,8,1],
    [6,8,3],
    [3,5,9]]
# result is 3x3
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
  
   for j in range(len(Y[0])):
    
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for res in result:
   print(res)

#Program to find the transpose of a matrix

X = [[1,2],
    [3 ,4],
    [5 ,6]]

result = [[0,0,0],
         [0,0,0]]


for i in range(len(X)):

   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


# prove (AB)'=B'A'

A = [[1,9,3],
    [9 ,5,6],
    [7 ,2,9]]
# 3x3 matrix
B = [[5,8,1],
    [6,8,3],
    [3,5,9]]
# result is 3x3
result1 = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(A)):
  
   for j in range(len(B[0])):
    
       for k in range(len(B)):
           result1[i][j] += A[i][k] * B[k][j]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(A)):

   for j in range(len(X[0])):
       result2[j][i] = A[i][j]

result3 = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(B)):

   for j in range(len(B[0])):
       result3[j][i] = B[i][j]

for i in range(len(result2)):
  
   for j in range(len(result3[0])):
    
       for k in range(len(result3)):
           result4[i][j] += result2[i][k] * result3[k][j]

if(result4[i][j]==result1[i][j])
    print("True")

else
    print("False")





