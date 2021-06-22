import numpy as np

A=[]
n=int(input("Enter N for N x N matrix: "))         
print("Enter the element ::>")
for i in range(n): 
   row=[]                                      
   for j in range(n): 
      row.append(int(input()))           
      A.append(row)                      
print(A)


print("Display Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(A[i][j], end=" ")
   print()                                        
B=[]
n=int(input("Enter N for N x N matrix : "))          

print("Enter the element ::>")
for i in range (n): 
   row=[]                                     
   for j in range(n): 
      row.append(int(input()))           
      B.append(row)                       
print(B)

print("Display Array In Matrix Form")
      
result = []
  

for i in range(len(A)): 
   for j in range(len(B[0])): 
      for k in range(len(B)): 
         result[i][j] += A[i][k] * B[k][j] 
print("The Resultant Matrix Is ::>")
for r in result: 
   print(r) 

X = []

for i in range(len(X)):

   for j in range(len(X[0])):
       A[j][i] = X[i][j]

for r in result:
   print("The transpose of first matrix is:")
   print(X)

Y = []

for i in range(len(X)):

   for j in range(len(X[0])):
       A[j][i] = Y[i][j]

for r in result:
   print("The transpose of second matrix is:")
   print(Y)

Z = []


for i in range(len(A)): 
   for j in range(len(B[0])): 
      for k in range(len(B)): 
        Z[i][j] += X[i][k] * Y[k][j] 
print("The Resultant Matrix Is ::>")
for r in result: 
   print(r) 

for i in range(len(Z)): 
   for j in range(len(result[0])): 
      for k in range(len(result)): 
        if(np.array_equal(Z,result))
        {
             print("Verified")
        }
           
        else
        { 
            print("False")
        }
          
