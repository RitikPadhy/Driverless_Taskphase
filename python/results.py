from Matrix_Operations import operations

    #Problem1
    A= [[1,9,3],
    [9 ,5,6],
    [7 ,2,9]]
    
    B = [[5,8,1],
    [6,8,3],
    [3,5,9]]

    C= calc_inv(B)
    for i in range(len(A)):
  
    for j in range(len(C[0])):
    
       for k in range(len(Y)):
           result[i][j] += A[i][k] * C[k][j]

         for res in result:
   print(res)  

        #Problem2

D= calc_inv(A)
    for i in range(len(D)):
  
    for j in range(len(C[0])):
    
       for k in range(len(Y)):
           result[i][j] += D[i][k] * C[k][j]

         for res1 in result:
   print(res1)  