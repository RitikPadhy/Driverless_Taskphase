from matrix_operations import operations

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
A = []
print("Enter the entries rowwise:")
  
for i in range(R):          
    a =[]
    for j in range(C):     
         a.append(int(input()))
    A.append(a)

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
B = []
print("Enter the entries rowwise:")
  
for i in range(R):          
    b =[]
    for j in range(C):     
         b.append(int(input()))
    B.append(b)



 adjoint = []
 adjoint1 = []
 inv = []
 inv1 = []
 res = []
 res1 = []

 
    operations.calc_adj(A, adjoint)
    operations.calc_adj(B, adjoint1)
    operations.calc_inv(A, inv)
    operations.calc_inv(B, inv1)

   for i in range(len(A)):
  
   for j in range(inv(B[0])):
    
       for k in range(inv(B)):
           res[i][j] += A[i][k] * inv[k][j]
    print(res)
    
    for i in range(len(inv)):
  
    for j in range(len(inv1[0])):
    
       for k in range(len(inv1)):
           res1[i][j] += inv[i][k] * inv1[k][j]
    print(res1)

  
